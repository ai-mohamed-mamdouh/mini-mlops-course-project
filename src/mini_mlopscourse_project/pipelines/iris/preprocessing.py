import numpy as np
from mini_mlopscourse_project.config.settings import settings
from mini_mlopscourse_project.schemas.iris.input_schema import input_schema

def pre_processing(input_data : input_schema) -> input_schema :
  
  input_data = input_data.features
  mean = np.load(settings.IRIS_MEAN_PATH)
  std = np.load(settings.IRIS_STD_PATH)

  # Apply the same normalization used during training
  input_data = (input_data - mean) / std

  input_data = np.array(
     input_data,
    dtype=np.float32
  )
  return input_schema(features=input_data)