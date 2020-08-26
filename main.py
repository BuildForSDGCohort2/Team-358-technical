#!/usr/bin/env python3 


# Importing the necessary modules 
import os 
import cv2
import time 
import joblib
import imutils 
import numpy as np
import tensorflow as tf
from imutils.video import VideoStream, FPS
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



# Getting the path to the seralized model and label files
# modelPath = "model/model3.h5"
modelPath = "model/GestureControl.h5"
# picklefile = "model/gestureLabels.pb"

# Creating the label encoder object
# lb = LabelEncoder() 

# Output features
numclasses = 4

# Creating the classes
classes = ['peace', 'three', 'thumbsup', 'unknown']


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



# Creating an instance of the VGGNet model
model = SmallerVGGNet().build(96, 96, 1, numclasses)


# Compiling the model
model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Loading the trained model weight file
model.load_weights(modelPath)

# loading the serialized pickle file
# lb = joblib.load(picklefile)

# Initialize the video stream and allow the camera sensor to warm up
print("[INFO] >> Starting the video stream.");
vs = VideoStream(src=0).start();

# Sleeping for 2 mili seconds
time.sleep(0.2)

# Starting the FPS counter
fps = FPS().start()

# loop over the frames from the video file stream
while True:
    # Grabbing the frames from the threaded video stream and resize it
    # to 500px (to speed up the processing)
    frame = vs.read()
    frame = imutils.resize(frame, width=500)

    # Cropping image
    cropped = frame[1:197, 285:493]  #y1, y2, x1, x2
    
    # Draw rect
    cv2.rectangle(frame, (285, 1), (493, 197), (255, 255, 0), 2)
    cv2.putText(frame, "Place your hands", (287, 220),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    # Convert the input from (1) BGR to grayscale
    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

    # Reshaping to dimension of (96, 96)
    gray = cv2.resize(gray, (96, 96), interpolation=cv2.INTER_AREA)
    img = img_to_array(gray)

    # Expanding dimensions
    img = np.expand_dims(img, axis=0)


    # Making predictions
    pred = model.predict(img)
    predClass = np.argmax(pred)
    
    # Getting the results
    result = classes[predClass]
    print(result) 

    # Describing the font to be used
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # Using put-text method to insert the predicted value on the video
    cv2.putText(frame, result, (9, 25), font, 0.72,
                                     (0, 0, 255), 2)

    # Displaying the image
    cv2.imshow("Image", frame)
    cv2.imshow("Cropped", cropped)

    # Existing
    key = cv2.waitKey(1) & 0xFF;
    if key == ord("q"):
        break
    
# Closing up and cleaning up
cv2.destroyAllWindows(); 
    


