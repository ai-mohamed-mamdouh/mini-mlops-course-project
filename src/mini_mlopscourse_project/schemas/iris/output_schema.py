from typing import List

from pydantic import BaseModel


class OutputSchema(BaseModel):
    """Schema describing predicted classes and class probabilities."""

    preds: List[int]
    proba: List[List[float]]