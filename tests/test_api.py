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

    # Assert status code
    assert response.status_code == 200

    # Assert response structure
    body = response.json()

    assert "preds" in body
    assert "proba" in body

    # Assert output format
    assert isinstance(body["preds"], list)
    assert isinstance(body["proba"], list)

    assert len(body["preds"]) == 1
    assert len(body["proba"]) == 1
    assert len(body["proba"][0]) == 3