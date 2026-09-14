from typing import List

from pydantic import BaseModel


class input_schema(BaseModel):
    """Schema describing the normalized Iris feature matrix for inference."""

    features: List[List[float]]