import onnxruntime as ort
from pathlib import Path


def loader(path: Path):
    """Load an ONNX model from a given path and return its inference session."""
    
    session = ort.InferenceSession(path)
    return session