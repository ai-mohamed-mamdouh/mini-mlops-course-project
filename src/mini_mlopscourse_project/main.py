from fastapi import FastAPI
from contextlib import asynccontextmanager
from mini_mlopscourse_project.api.iris.routes import iris_router
from mini_mlopscourse_project.models.factory import ModelFactory


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load model once when application starts
    print("Loading model...")

    # Load model once
    app.state.iris_model = ModelFactory.create("iris")

    yield

    # Cleanup if needed
    app.state.iris_model = None
    print("Shutdown...")


app = FastAPI(
    title="ML Inference API",
    lifespan=lifespan, 
    
)

app.include_router(iris_router)