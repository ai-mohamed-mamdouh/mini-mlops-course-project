from pydantic import BaseModel
from typing import List

class output_schema(BaseModel):
    preds: List[int]
    proba: List[List[float]]