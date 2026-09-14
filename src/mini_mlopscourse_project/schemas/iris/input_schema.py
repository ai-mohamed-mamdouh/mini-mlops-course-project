from pydantic import BaseModel
from typing import List

class input_schema(BaseModel):
    features: List[List[float]]