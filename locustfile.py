import random
from locust import HttpUser, task, between


class APIUser(HttpUser):
    wait_time = between(0.5, 1.5)

    @task
    def predict(self):

        features = [
            [
                random.uniform(0, 5),
                random.uniform(0, 5),
                random.uniform(0, 5),
                random.uniform(0, 5)
            ]
        ]

        payload = {
            "features": features
        }

        self.client.post(
            "/predict/iris/predict",
            json=payload
        )