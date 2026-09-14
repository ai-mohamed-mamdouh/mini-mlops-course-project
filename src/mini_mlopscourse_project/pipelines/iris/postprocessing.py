import numpy as np
from mini_mlopscourse_project.schemas.iris.output_schema import output_schema


def post_processing(logits) -> output_schema:
    """Convert model logits into class predictions and probabilities."""

    def softmax(x):
        """Apply softmax across the class dimension for each sample."""
        
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)

    proba = softmax(logits)
    preds = np.argmax(proba, axis=1)

    return output_schema(preds=preds, proba=proba)
