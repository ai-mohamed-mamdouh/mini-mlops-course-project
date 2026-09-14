from models.base import BaseModel

class IrisModel(BaseModel):

    def __init__(self, session):
        self.session = session

    def predict(self, x):
        output = session.run(
                ["output"],          # Output tensor name

                {
                    "input": input_data.features  # Input tensor name and data
                }
            )

        return output