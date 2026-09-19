import numpy as np
from mini_mlopscourse_project.config.settings import settings
from mini_mlopscourse_project.processors.base import PipelineStep
from mini_mlopscourse_project.schemas.iris.input_schema import InputSchema
from mini_mlopscourse_project.core.exceptions import(
    PreprocessingError,
    )


class PreprocessingStep(PipelineStep) :
    def __init__(self):

        self.mean = np.load(settings.IRIS_MEAN_PATH)
        self.std = np.load(settings.IRIS_STD_PATH)


    def run(
        self,
        input_data: InputSchema
    ) -> InputSchema:
        """
        Normalize Iris features using training statistics.
        """
        try:
            features = np.array(
                input_data.features,
                dtype=np.float32
            )
            features = (features - self.mean) / self.std
            return InputSchema(features=features)
        
        except Exception as e:
            raise PreprocessingError(
                "Cannot make PreProcessing"
            ) from e