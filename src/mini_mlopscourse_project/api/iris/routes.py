from fastapi import APIRouter, Request
from mini_mlopscourse_project.schemas.iris.input_schema import input_schema
from mini_mlopscourse_project.schemas.iris.output_schema import output_schema
from mini_mlopscourse_project.pipelines.iris.preprocessing import pre_processing
from mini_mlopscourse_project.pipelines.iris.postprocessing import post_processing



iris_router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)


@iris_router.post("/iris/predict")
def predict(
    data: input_schema,
    request: Request
)->output_schema:
    iris_model = request.app.state.iris_model

    input_data = pre_processing(input_data=data)
    logits = iris_model.predict(input_data=input_data)

    output = post_processing(logits=logits)

    return output

