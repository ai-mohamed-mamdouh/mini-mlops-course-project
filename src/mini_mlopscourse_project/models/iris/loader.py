import onnxruntime as ort
from pathlib import Path
from mini_mlopscourse_project.core.logging import get_logger 
from mini_mlopscourse_project.core.logging import get_logger
from mini_mlopscourse_project.core.exceptions import ( ModelLoadError )


def loader(path: Path):
    """Load an ONNX model from a given path and return its inference session."""

    try:
        logger = get_logger(__name__)
        logger.info(
            f"Loading model from {path}"
        )
        session = ort.InferenceSession(path)
        logger.info(
            "Model loaded successfully"
        )
        return session

    except Exception as e:
        logger.exception(
            'load model failed'
        )
        raise ModelLoadError(
            "Cannot load model"
        ) from e