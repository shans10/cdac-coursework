import tensorflow as tf
import keras
import torch

print("TensorFlow version:", tf.__version__)
print("Keras version:", keras.__version__)
print("PyTorch version:", torch.__version__)

print("TensorFlow is using GPU:", tf.test.is_gpu_available())
print("PyTorch is using GPU:", torch.cuda.is_available())
