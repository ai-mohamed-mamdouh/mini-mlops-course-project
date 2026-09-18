import onnxruntime as ort
from pathlib import Path
from mini_mlopscourse_project.core.exceptions import ( ModelLoadError )


def loader(path: Path):
    """Load an ONNX model from a given path and return its inference session."""

    try:
        session = ort.InferenceSession(path)
        return session

    except Exception as e:
        raise ModelLoadError(
            "Cannot load model"
        ) from e