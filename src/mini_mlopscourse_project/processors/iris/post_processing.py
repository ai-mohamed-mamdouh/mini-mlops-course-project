import numpy as np
from mini_mlopscourse_project.processors.base import PipelineStep
from mini_mlopscourse_project.schemas.iris.output_schema import OutputSchema
from mini_mlopscourse_project.core.exceptions import(
    PostprocessingError
    )

class PostprocessingStep(PipelineStep):
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
        