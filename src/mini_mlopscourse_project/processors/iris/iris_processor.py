import numpy as np
from mini_mlopscourse_project.config.settings import settings
from mini_mlopscourse_project.schemas.iris.input_schema import InputSchema
from mini_mlopscourse_project.schemas.iris.output_schema import OutputSchema
from mini_mlopscourse_project.core.exceptions import(
    PreprocessingError,
    PostprocessingError
    )


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

    @staticmethod
    def post_processing(
        logits: np.ndarray
    ) -> list[OutputSchema]:
        """
        Convert batch logits into individual responses.
        """
        try: 
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

            results = []
            for pred, prob in zip(
                preds,
                proba
            ):
                results.append(
                    OutputSchema(
                        preds=[int(pred)],
                        proba=[prob.tolist()]
                    )
                )
            return results
        
        except Exception as e:
            raise PostprocessingError(
                "Cannot make PostProcessing"
            ) from e
