from abc import ABC, abstractmethod
from pydantic import BaseModel


class BaseModel(ABC):
    """Abstract interface for all model implementations in the project."""

    @abstractmethod
    def predict(self, input_data: BaseModel) -> BaseModel:
        """Run inference for a given input payload and return a model output."""
        pass