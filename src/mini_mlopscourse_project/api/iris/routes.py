from fastapi import APIRouter, Request, Header
from mini_mlopscourse_project.schemas.iris.input_schema import InputSchema
from mini_mlopscourse_project.schemas.iris.output_schema import OutputSchema


iris_router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)


@iris_router.post("/iris/predict")
async def predict(
    input_data: InputSchema,
    request: Request,
    # x: int = Header()
)->OutputSchema:

    result = await request.app.state.batch_manager.add_request(
        input_data
    )

    return result
