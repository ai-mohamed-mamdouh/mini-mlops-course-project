from mini_mlopscourse_project.models.base import BaseModel
from mini_mlopscourse_project.schemas.iris.input_schema import input_schema


class IrisModel(BaseModel):
    """Wrapper around the trained Iris ONNX model for inference."""

    def __init__(self, session):
        """Store the ONNX inference session used by the model."""
        self.session = session

    def predict(self, input_data: input_schema):
        """Run inference for a feature vector and return the model logits."""
        
        logits = self.session.run(
            ["output"],
            {"input": input_data.features},
        )

        return logits[0]