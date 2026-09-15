import numpy as np

from mini_mlopscourse_project.config.settings import settings
from mini_mlopscourse_project.schemas.iris.input_schema import InputSchema
from mini_mlopscourse_project.schemas.iris.output_schema import OutputSchema


class IrisProcessor:

    def __init__(self):

        self.mean = np.load(settings.IRIS_MEAN_PATH)
        self.std = np.load(settings.IRIS_STD_PATH)


    def pre_processing(
        self,
        input_data: InputSchema
    ) -> InputSchema:
        """
        Normalize Iris features using training statistics.
        """

        features = np.array(
            input_data.features,
            dtype=np.float32
        )

        features = (features - self.mean) / self.std

        return InputSchema(features=features)


    @staticmethod
    def post_processing(
        logits: np.ndarray
    ) -> OutputSchema:
        """
        Convert logits into predictions and probabilities.
        """

        exp_x = np.exp(
            logits - np.max(logits, axis=1, keepdims=True)
        )

        proba = exp_x / np.sum(
            exp_x,
            axis=1,
            keepdims=True
        )

        preds = np.argmax(
            proba,
            axis=1
        )

        return OutputSchema(
            preds=preds.tolist(),
            proba=proba.tolist()
        )