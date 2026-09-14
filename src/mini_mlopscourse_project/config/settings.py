from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # Project root
    BASE_DIR: Path = Path(__file__).resolve().parents[3]

    # Artifacts
    ARTIFACTS_DIR: Path = BASE_DIR / "artifacts"

    # Iris model
    IRIS_MODEL_PATH: Path = (
        ARTIFACTS_DIR 
        / "iris"
        / "iris.onnx"
    )
    IRIS_MEAN_PATH: Path = (
        ARTIFACTS_DIR 
        / "iris"
        / "mean.npy"
    )
    IRIS_STD_PATH: Path = (
        ARTIFACTS_DIR 
        / "iris"
        / "std.npy"
    )

settings = Settings()