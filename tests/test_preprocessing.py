from mini_mlopscourse_project.schemas.iris.input_schema import InputSchema
from mini_mlopscourse_project.processors.iris.iris_processor import IrisProcessor


def test_iris_preprocessing():

    # Arrange
    input_data = InputSchema(
        features=[ [1, 2, 3, 4] ]
    )

    # Act
    result = IrisProcessor().pre_processing(input_data)

    # Assert
    assert isinstance(result, InputSchema)

    assert isinstance(result.features, list)
    assert isinstance(result.features[0], list)

    assert len(result.features) == 1
    assert len(result.features[0]) == 4