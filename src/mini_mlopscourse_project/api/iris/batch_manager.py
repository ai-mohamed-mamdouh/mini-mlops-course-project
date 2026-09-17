import asyncio
from mini_mlopscourse_project.schemas.iris.input_schema import InputSchema
from mini_mlopscourse_project.services.iris.iris_service import IrisService

class BatchManager:

    def __init__(
        self,
        iris_service: IrisService,
        max_batch_size=10,
        timeout=0.01
    ):
        self.iris_service = iris_service

        self.max_batch_size = max_batch_size
        self.timeout = timeout

        self.queue = []


    async def add_request(
        self,
        input_data: InputSchema
    ):

        future = asyncio.Future()

        self.queue.append(
            (
                input_data,
                future
            )
        )

        return await future



    async def process_batch(self):

        while True:

            await asyncio.sleep(
                self.timeout
            )


            if not self.queue:
                continue


            # take batch
            batch_items = self.queue[:self.max_batch_size]

            self.queue = self.queue[self.max_batch_size:]


            inputs = [
                item[0]
                for item in batch_items
            ]


            futures = [
                item[1]
                for item in batch_items
            ]


            # merge requests
            batch_features = []

            for input_data in inputs:

                batch_features.extend(
                    input_data.features
                )


            batch_input = InputSchema(
                features=batch_features
            )
            results = self.iris_service.run_iris_service(batch_input)

            # return each result
            for future, result in zip(
                futures,
                results
            ):

                future.set_result(
                    result
                )