from fastapi import APIRouter, Request, Header
from mini_mlopscourse_project.schemas.iris.input_schema import InputSchema
from mini_mlopscourse_project.schemas.iris.output_schema import OutputSchema
from mini_mlopscourse_project.memory.cache.redis_service import RedisService

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
    redis_service = RedisService( request.app.state.redis_client )
    result = redis_service.get_prediction(input_data.features)

    if result :
        print('found result in cache >>>')
        return result
    else:
        print('not found result in cache >>>')
        result = await request.app.state.batch_manager.add_request(
            input_data
        )
        redis_service.save_prediction(input_data.features, result.model_dump())

    return result
