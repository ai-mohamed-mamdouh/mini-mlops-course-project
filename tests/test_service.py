from mini_mlopscourse_project.services.iris.iris_service import IrisService
from mini_mlopscourse_project.models.factory import ModelFactory
from mini_mlopscourse_project.processors.iris.iris_processor import IrisProcessor
from mini_mlopscourse_project.schemas.iris.input_schema import InputSchema
from mini_mlopscourse_project.schemas.iris.output_schema import OutputSchema

def test_iris_service() :
    input_data = InputSchema(features=[ [1,2,3,4] ])

    result = IrisService(
        ModelFactory.create('iris'),
        iris_processor=IrisProcessor()
        ).run_iris_service(input_data=input_data)

    # Assert
    assert isinstance(result, OutputSchema)

    assert isinstance(result.preds, list)
    assert isinstance(result.proba, list)

    assert result.preds == [2]

    assert len(result.proba) == 1
    assert len(result.proba[0]) == 3
    