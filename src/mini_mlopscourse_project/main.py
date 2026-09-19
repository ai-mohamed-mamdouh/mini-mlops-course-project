import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager
from mini_mlopscourse_project.api.iris.routes import iris_router
from mini_mlopscourse_project.core.logging import setup_logging
from mini_mlopscourse_project.models.factory import ModelFactory
from mini_mlopscourse_project.core.exceptions import PredictionError
from mini_mlopscourse_project.api.batch_manager import BatchManager
from mini_mlopscourse_project.services.iris.iris_service import IrisPipeline
from mini_mlopscourse_project.api.error_handlers import prediction_error_handler
from mini_mlopscourse_project.processors.iris.pre_processing import PreprocessingStep
from mini_mlopscourse_project.processors.iris.post_processing import PostprocessingStep
from mini_mlopscourse_project.processors.iris.model_processing import ModelPredictionStep

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load model once when application starts
    model = ModelFactory.create("iris")

    iris_service = IrisPipeline(
        [
        PreprocessingStep(),
        ModelPredictionStep(iris_model=model),
        PostprocessingStep()
        ]
        )

    batch_manager = BatchManager(iris_service=iris_service)
    app.state.batch_manager = batch_manager

    asyncio.create_task(
        batch_manager.process_batch()
    )

    yield

    # Cleanup if needed
    model = None
    iris_service = None
    app.state.batch_manager = None
    

setup_logging()

app = FastAPI(
    title="ML Inference API",
    lifespan=lifespan, 
    
)

app.add_exception_handler(
    PredictionError,
    prediction_error_handler
)

app.include_router(iris_router)
