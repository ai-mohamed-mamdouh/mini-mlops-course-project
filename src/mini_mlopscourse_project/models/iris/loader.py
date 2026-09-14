import onnxruntime as ort
from pathlib import Path
from mini_mlopscourse_project.config.settings import settings

# Load ONNX model
def loader(path:Path) :
    session = ort.InferenceSession( path )

    return session