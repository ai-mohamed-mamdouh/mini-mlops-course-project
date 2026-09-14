from models.iris.loader import load_model
from models.iris.model import IrisModel
from config.settings import settings


class ModelFactory:

    @staticmethod
    def create(name):

        if name == "iris":

            session = load_model(
                settings.IRIS_MODEL_PATH
            )

            return IrisModel(session)