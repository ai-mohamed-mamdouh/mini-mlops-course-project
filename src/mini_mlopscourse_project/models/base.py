from abc import ABC, abstractmethod
from pydantic import BaseModel

class BaseModel(ABC) :
    @abstractmethod
    def predict(self, input_data : BaseModel) -> BaseModel :
        pass