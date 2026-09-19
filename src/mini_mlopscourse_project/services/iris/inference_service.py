from mini_mlopscourse_project.schemas.iris.input_schema import InputSchema
from mini_mlopscourse_project.schemas.iris.output_schema import OutputSchema

class IrisPipeline : 
    def __init__(self, steps : list) :
        self.steps = steps

    def run(self, input_data: InputSchema) -> list[OutputSchema] : 
        
        data = input_data
        for step in self.steps :
            data = step.run(data)

        return data
