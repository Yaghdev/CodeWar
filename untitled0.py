from detector.face_detector import MTCNNFaceDetector
from models.elg_keras import KerasELG
from keras import backend as K

import numpy as np
import cv2
import keras2onnx
from matplotlib import pyplot as plt   


import onnxruntime
model = KerasELG()
model.net.load_weights("./elg_weights/elg_keras.h5")
onnx_model = keras2onnx.convert_keras(model.net, model.net.name)
temp_model_file = './model.onnx'
keras2onnx.save_model(onnx_model, temp_model_file)
