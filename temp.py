from keras.models import Sequential
from keras.layers import Dense, Flatten, Activation, Dropout, Conv2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
import keras
import cv2
from sklearn.model_selection import train_test_split 
from keras.utils import np_utils
IMG_SIZE = 64
import os
import numpy as np
#import keras2onnx
import random
import shutil
 
def load_data():
	images = []
	label = []
	print("Loading Data................")
	for row in os.listdir('/home/ubuntu/eye_estimate/Binary-Classification/dataset/mrlEyes_2018_01'):
		for sub_row in os.listdir('/home/ubuntu/eye_estimate/Binary-Classification/dataset/mrlEyes_2018_01/'+str(row)):
			
			img = cv2.imread('/home/ubuntu/eye_estimate/Binary-Classification/dataset/mrlEyes_2018_01/'+str(row)+"/"+str(sub_row))
			img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)			 
			img = cv2.resize(img, (32, 32))
			img = np.expand_dims(np.array(img), axis=2)
			img = img / 255			 
			images.append(img)			 
			label.append(int(str(sub_row).split("_")[4]))
		 
	X_train, X_test, y_train, y_test = train_test_split(np.array(images), label, test_size=0.30, random_state=42)
	return np.array(X_train), np.array(X_test), np.expand_dims(np.array(y_train), axis=1), np.expand_dims(np.array(y_test), axis=1)  

X_train, X_test, y_train, y_test = load_data()

print('x_train shape:', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

# X_train = np.array(X_train).astype('float32')
# X_test = np.array(X_test).astype('float32')
 
y_train = np_utils.to_categorical(y_train, num_classes=1)
y_test = np_utils.to_categorical(y_test, num_classes=1)



# train_datagen = ImageDataGenerator(rescale=1./255,shear_range=0.2, zoom_range=[0.9, 1.25] )

# val_datagen = ImageDataGenerator(rescale=1./255,shear_range=0.2, zoom_range=[0.9, 1.25])

# train_generator = train_datagen.flow_from_directory(directory="dataset/training_set",target_size=(IMG_SIZE, IMG_SIZE),
# 	color_mode="grayscale", batch_size=16,class_mode="binary",shuffle=True,seed=42)

# val_generator = val_datagen.flow_from_directory(directory="dataset/test_set",target_size=(IMG_SIZE, IMG_SIZE),
# 	color_mode="grayscale", batch_size=16,class_mode="binary",shuffle=True,seed=42)



# STEP_SIZE_TRAIN=train_generator.n//train_generator.batch_size
# STEP_SIZE_VALID=val_generator.n//val_generator.batch_size

#Intialize Neural Network'

model = Sequential()
 

model.add(Conv2D(16, (3, 3), input_shape=(32, 32, 1), activation='relu', padding='same'))
model.add(Dropout(0.2))
model.add(Conv2D(16, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(Dropout(0.2))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1, activation='softmax'))
 
model.summary()

checkpoint = keras.callbacks.ModelCheckpoint('./checkpoint/model{epoch:08d}.h5') 

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, batch_size=32, epochs=1000, callbacks=[checkpoint], validation_data=(X_test,y_test), shuffle=True)

# model.fit_generator(generator=train_generator,
# 		    callbacks=[checkpoint],
# 		    steps_per_epoch=STEP_SIZE_TRAIN,
# 		    validation_data=val_generator,
# 		    validation_steps=STEP_SIZE_VALID,
# 		    epochs=100)
print("converting.............")
#onnx_model = keras2onnx.convert_keras(model, model.name)
#import onnx
#onnx.save_model(onnx_model, './fish-resnet50.onnx')
model.save_weights("model.h5")