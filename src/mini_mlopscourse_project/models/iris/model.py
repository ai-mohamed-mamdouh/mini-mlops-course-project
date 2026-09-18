from mini_mlopscourse_project.models.base import BaseModel
from mini_mlopscourse_project.schemas.iris.input_schema import InputSchema
from mini_mlopscourse_project.core.exceptions import ( PredictionError )

class IrisModel(BaseModel):
    """Wrapper around the trained Iris ONNX model for inference."""

    def __init__(self, session):
        """Store the ONNX inference session used by the model."""
        self.session = session

    def predict(self, input_data: InputSchema):
        """Run inference for a feature vector and return the model logits."""
        try:
            logits = self.session.run(
                ["output"],
                {"input": input_data.features},
            )
            return logits[0]

        except Exception as e:
            raise PredictionError(
                "Cannot make predict"
            ) from e
