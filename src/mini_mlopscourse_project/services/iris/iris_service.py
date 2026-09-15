from mini_mlopscourse_project.processors.iris.iris_processor import IrisProcessor
from mini_mlopscourse_project.models.factory import ModelFactory
from mini_mlopscourse_project.models.iris.model import IrisModel
from mini_mlopscourse_project.schemas.iris.input_schema import InputSchema
from mini_mlopscourse_project.schemas.iris.output_schema import OutputSchema

class IrisService : 
    def __init__(self, iris_model: IrisModel, iris_processor: IrisProcessor) :
        self.iris_model = iris_model
        self.iris_processor = iris_processor

    def run_iris_service(self, input_data: InputSchema) -> OutputSchema : 
        features = self.iris_processor.pre_processing(input_data=input_data)

        logits = self.iris_model.predict(features)

        output = self.iris_processor.post_processing(logits)

        return output