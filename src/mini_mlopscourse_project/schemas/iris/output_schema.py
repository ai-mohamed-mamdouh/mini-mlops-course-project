from typing import List

from pydantic import BaseModel


class output_schema(BaseModel):
    """Schema describing predicted classes and class probabilities."""

    preds: List[int]
    proba: List[List[float]]