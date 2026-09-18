class MLServiceError(Exception):
    """
    Base exception for ML service errors.
    """
    pass

class ModelLoadError(MLServiceError):
    """
    Raised when loading the ML model fails.
    """
    pass

class PredictionError(MLServiceError):
    """
    Raised when model inference fails.
    """
    pass

class PreprocessingError(MLServiceError):
    """
    Raised when input preprocessing fails.
    """
    pass

class PostprocessingError(MLServiceError):
    """
    Raised when output postprocessing fails.
    """
    pass