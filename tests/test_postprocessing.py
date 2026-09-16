import numpy as np

from mini_mlopscourse_project.processors.iris.iris_processor import IrisProcessor
from mini_mlopscourse_project.schemas.iris.output_schema import OutputSchema


def test_iris_postprocessing():

    # Arrange
    logits = np.array([
        [1.0, 2.0, 5.0]
    ])

    # Act
    result = IrisProcessor().post_processing(logits)

    # Assert
    assert isinstance(result, OutputSchema)

    assert isinstance(result.preds, list)
    assert isinstance(result.proba, list)

    assert result.preds == [2]

    assert len(result.proba) == 1
    assert len(result.proba[0]) == 3