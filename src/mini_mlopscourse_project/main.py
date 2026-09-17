from fastapi import FastAPI
import asyncio
from contextlib import asynccontextmanager
from mini_mlopscourse_project.api.iris.batch_manager import BatchManager
from mini_mlopscourse_project.api.iris.routes import iris_router
from mini_mlopscourse_project.models.factory import ModelFactory
from mini_mlopscourse_project.processors.iris.iris_processor import IrisProcessor


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load model once when application starts
    print("Loading model...")

    # Load model once
    model = ModelFactory.create("iris")
    processor = IrisProcessor()
    batch_manager = BatchManager(model = model
                                 ,processor=processor)
    app.state.batch_manager = batch_manager

    asyncio.create_task(
        batch_manager.process_batch()
    )

    yield

    # Cleanup if needed
    app.state.iris_model = None
    print("Shutdown...")


app = FastAPI(
    title="ML Inference API",
    lifespan=lifespan, 
    
)

app.include_router(iris_router)