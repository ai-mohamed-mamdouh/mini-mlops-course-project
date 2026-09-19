from mini_mlopscourse_project.models.iris.model import IrisModel
from mini_mlopscourse_project.processors.base import PipelineStep
from mini_mlopscourse_project.schemas.iris.input_schema import InputSchema
import numpy as np

class ModelPredictionStep(PipelineStep) :

    def __init__(self, iris_model: IrisModel) :
        self.iris_model = iris_model

    def run(self, input_data: InputSchema) -> np.ndarray : 
        logits = self.iris_model.predict(input_data)

        return logits
