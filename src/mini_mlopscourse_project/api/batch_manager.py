import asyncio
from mini_mlopscourse_project.schemas.iris.input_schema import InputSchema
from mini_mlopscourse_project.services.iris.inference_service import IrisPipeline


class BatchManager:
    """Collects incoming prediction requests and processes them in batches.

    The manager buffers requests until the configured batch size is reached or
    enough time has passed, then sends a combined input to the Iris service and
    resolves each queued request with its corresponding result.
    """

    def __init__(
        self,
        iris_service: IrisPipeline,
        max_batch_size=10,
        timeout=0.01
    ):
        """Initialize the batch manager with the service and batching settings.

        Args:
            iris_service: The service implementation used to execute a batched
                prediction request.
            max_batch_size: Maximum number of requests to combine in a single
                batch.
            timeout: Delay between queue checks used by the background processing
                loop.
        """
        self.iris_service = iris_service

        self.max_batch_size = max_batch_size
        self.timeout = timeout

        self.queue = []

    async def add_request(
        self,
        input_data: InputSchema
    ):
        """Queue a single prediction request and await its result.

        Args:
            input_data: Input payload containing the feature vector for one
                prediction request.

        Returns:
            The prediction result produced for this request after the batch is
            processed.
        """
        future = asyncio.Future()

        self.queue.append(
            (
                input_data,
                future
            )
        )

        return await future

    async def process_batch(self):
        """Continuously drain queued requests into batches and resolve them.

        This background loop waits for requests to accumulate, builds one combined
        InputSchema for the batch, submits it to the underlying Iris service, and
        then fulfills each waiting future with the corresponding prediction.
        """
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
            results = self.iris_service.run(batch_input)

            # return each result
            for future, result in zip(
                futures,
                results
            ):

                future.set_result(
                    result
                )