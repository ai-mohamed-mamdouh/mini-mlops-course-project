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
    redis_service = request.app.state.redis_service
    result = redis_service.get_prediction(input_data.features)

    if result :
        return result
    else:
        result = await request.app.state.batch_manager.add_request(
            input_data
        )
        redis_service.save_prediction(input_data.features, result.model_dump())

    return result
