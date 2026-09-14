
from mini_mlopscourse_project.models.iris.loader import loader
from mini_mlopscourse_project.models.iris.model import IrisModel
from mini_mlopscourse_project.config.settings import settings


class ModelFactory:

    @staticmethod
    def create(name):

        if name == "iris":

            session = loader(
                settings.IRIS_MODEL_PATH
            )

            return IrisModel(session)