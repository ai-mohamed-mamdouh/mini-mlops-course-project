from mini_mlopscourse_project.models.base import BaseModel
from mini_mlopscourse_project.schemas.iris.input_schema import input_schema
class IrisModel(BaseModel):

    def __init__(self, session):
        self.session = session

    def predict(self, input_data : input_schema):
        output = self.session.run(
                ["output"],          # Output tensor name

                {
                    "input": input_data.features  # Input tensor name and data
                }
            )

        return output