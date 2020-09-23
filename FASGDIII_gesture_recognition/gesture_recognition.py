#!/usr/bin/env python3 

# Author: Mbonu Chinedum Endurance 
# Team: TEAM-358-GROUP-A
# Description: FASGD-III (Gesture Recognition Model)
# Program: ANDELA BUILD FOR SDG COHORT-2 2020
# Country: Nigeria 
# Date Created: 27-August-2020  "Buhari Regime"
# Date Modified: 


# Importing the necessary modules
import os 
import cv2
import joblib as jb
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from sklearn.preprocessing import LabelEncoder
from .build_model import SmallerVGGNet
  

# Global variables 
bg = None 


# Creating a class for gesture prediction 
class GesturePredict: 
    def __init__(self, input_image):
        # Grabbing the input image 
        self.image = input_image 

        # Setting some parameters for the model 
        self.img_dim = (96, 96, 1)
        self.num_class = 7 

        # Getting the path to the serialized label encoder 
        self.lb = os.path.sep.join(["FASGDIII_gesture_recognition", "encoder/lb_encoder"])

        # Getting the path to the serialized model weight file 
        self.model_path = os.path.sep.join(["FASGDIII_gesture_recognition", "model/hand_gesture.h5"])

    # Creating a method for compiling and building the serialized model 
    def gesture_model(self): 
        # Building the Gesture model 
        model = SmallerVGGNet().build(self.img_dim[1], self.img_dim[0], 
                                        self.img_dim[2], self.num_class) 
        # Compiling the Gesture model 
        model.compile(optimizer='adam', 
                            loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                            metrics=['accuracy'])

        # Loading the serialized model 
        model.load_weights(self.model_path) 

        # Returning the model 
        return model 

    # Creating a method for loading the encoder model 
    def load_encoder(self): 
        # Creating the label encoder object 
        lb = LabelEncoder() 

        # loading the serialized encoder object 
        lb = jb.load(self.lb) 

        # Returning the loaded encoder model 
        return lb 

    # Creating a method for predictions 
    def make_predictions(self, image): 
        # Resizing the image to dim (96, 96)
        image = cv2.resize(image, (96, 96))

        # Converting the image into an array 
        image = img_to_array(image)

        # Expanding the image dimensions
        image = np.expand_dims(image, axis = 0)
        
        # Creating an instance of the gesture and encoder model weight file 
        model = self.gesture_model()
        lb = self.load_encoder() 

        # Making predictions 
        result = np.argmax(model.predict(image)) 
        result = lb.classes_[result]

        # Returning the predicted class 
        return result  

    # Finding the running average over the background 
    def run_avg(self, aWeight):
        global bg 
        # Initialize the background 
        if bg is None: 
            # Get the background-image 
            bg = self.image.copy().astype("float32")
            
            # Compute the weighted average, accumulate it and update the background  
            return
            cv2.accumulatedWeighted(self.image, bg, aWeight)

    # To segment the region of hand in the image  
    def segment(self, threshold=25):
        global bg 
        # Find the absolute difference between background and current frame 
        diff = cv2.absdiff(bg.astype("uint8"), self.image)
        
        # Threshold the diff image so that we get the foreground
        thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]

        # Getting the contours in the thresholded image
        (cnts, hierarchy) = cv2.findContours(thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Return None, if no countors detected
        if len(cnts) == 0:
            return None
        else:
            # Based on contour area, get the maximum contour whihc is the HAND
            segmented = max(cnts, key=cv2.contourArea)
            return (thresholded, segmented)

