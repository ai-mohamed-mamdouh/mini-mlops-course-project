from mini_mlopscourse_project.models.iris.loader import loader
from mini_mlopscourse_project.models.iris.model import IrisModel
from mini_mlopscourse_project.config.settings import settings


class ModelFactory:
    """Create configured model instances for supported project models."""

    @staticmethod
    def create(name):
        """Instantiate and return a model by its registered name."""
        
        if name == "iris":
            session = loader(settings.IRIS_MODEL_PATH)
            return IrisModel(session)

        raise ValueError(f"Unsupported model name: {name}")