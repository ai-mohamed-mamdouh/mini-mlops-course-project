from fastapi.testclient import TestClient

from mini_mlopscourse_project.main import app


def test_iris_prediction():

    with TestClient(app) as client:

        response = client.post(
            "/predict/iris/predict",
            json={
                "features": [
                    [1, 2, 3, 4]
                ]
            }
        )

        assert response.status_code == 200

        body = response.json()

        assert "preds" in body
        assert "proba" in body