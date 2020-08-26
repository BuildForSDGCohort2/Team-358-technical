#!/usr/bin/env python
# coding: utf-8 

# Importing the necessary modules 
import os 
import cv2 
import random 
import numpy as np
import joblib 
import keras
import tensorflow as tf 
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras import backend as K
from imutils import paths 
from tensorflow.keras.optimizers import Adam 
from tensorflow.keras.preprocessing.image import img_to_array, ImageDataGenerator 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler, LabelEncoder 
from tensorflow.keras.optimizers import SGD 
from tensorflow.keras.layers import Flatten, MaxPool2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical 
from tensorflow.keras.layers import Conv2D, Dense, Activation, Dropout 


# Initialize the data and labels 
data = np.load("datasets/data.npy")
labels = np.load("datasets/encoded_labels.npy")


# Splitting the features into training and testing splits using 80% of 
# the data for training and the remaining 20% for testing 
(X_train, X_test, y_train, y_test) = train_test_split(data, labels, 
                                                     test_size=0.33, random_state=42)

# Displaying the shape of both the input and output features 
print("Input Shape: {}, {}".format(X_train.shape, X_test.shape)) 
print("Output Shape: {}, {}".format(y_train.shape, y_test.shape))


# Building the VGGNet model 
class SmallerVGGNet:
    @staticmethod
    def build(width, height, depth, classes, finalAct="softmax"):
        # initialize the model along with the input shape to be
        # "channels last" and the channels dimension itself
        model = Sequential()
        inputShape = (height, width, depth)
        chanDim = -1
        
        # CONV => RELU => POOL
        model.add(Conv2D(32, (3, 3), padding="same",
            input_shape=inputShape))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(MaxPooling2D(pool_size=(3, 3)))
        model.add(Dropout(0.25))

        # (CONV => RELU) * 2 => POOL
        model.add(Conv2D(64, (3, 3), padding="same"))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(Conv2D(64, (3, 3), padding="same"))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        # (CONV => RELU) * 2 => POOL
        model.add(Conv2D(128, (3, 3), padding="same"))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(Conv2D(128, (3, 3), padding="same"))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        # first (and only) set of FC => RELU layers
        model.add(Flatten())
        model.add(Dense(1024))
        model.add(Activation("relu"))
        model.add(BatchNormalization())
        model.add(Dropout(0.5))

        # softmax classifier
        model.add(Dense(classes))
        model.add(Activation(finalAct))

        # return the constructed network architecture
        return model
    

# Setting the number of classes as 7 
numclasses = 7

# Creating an instance of the VGGNet model 
model = SmallerVGGNet().build(96, 96, 1, numclasses)


# Compiling the model 
model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])


# Training the model
print("Training The model \n ----------------------------------------------------------------------------")
H = model.fit(X_train, y_train, epochs = 20, batch_size=5, validation_data=(X_test, y_test), verbose=1)


# Saving the trained model weight file 
model.save_weights("model/GestureControl.h5")

