import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager
from mini_mlopscourse_project.core.logging import setup_logging
from mini_mlopscourse_project.api.iris.routes import iris_router
from mini_mlopscourse_project.models.factory import ModelFactory
from mini_mlopscourse_project.services.iris.iris_service import IrisService
from mini_mlopscourse_project.api.batch_manager import BatchManager
from mini_mlopscourse_project.processors.iris.iris_processor import IrisProcessor
from mini_mlopscourse_project.core.exceptions import PredictionError
from mini_mlopscourse_project.api.error_handlers import prediction_error_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load model once when application starts
    # Load model once
    model = ModelFactory.create("iris")
    processor = IrisProcessor()

    iris_service = IrisService(
        iris_model=model,
        iris_processor=processor
    )

    batch_manager = BatchManager(iris_service=iris_service)
    app.state.batch_manager = batch_manager

    asyncio.create_task(
        batch_manager.process_batch()
    )

    yield

    # Cleanup if needed
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