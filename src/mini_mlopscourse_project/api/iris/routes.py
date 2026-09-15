from fastapi import APIRouter, Request, Header

from mini_mlopscourse_project.services.iris.iris_service import IrisService
from mini_mlopscourse_project.schemas.iris.input_schema import InputSchema
from mini_mlopscourse_project.schemas.iris.output_schema import OutputSchema


iris_router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)


@iris_router.post("/iris/predict")
def predict(
    input_data: InputSchema,
    request: Request,
    # x: int = Header()
)->OutputSchema:
    
    output = IrisService(
        iris_model=request.app.state.iris_model,
        iris_processor=request.app.state.iris_processor
        ).run_iris_service(input_data=input_data)


    return output
