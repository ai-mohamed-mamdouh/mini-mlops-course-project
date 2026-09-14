import onnxruntime as ort
from config.settings import settings

# Load ONNX model
def loader(path:str) :
    session = ort.InferenceSession( path )

    return session