#!/usr/bin/env python3

# Author: Mbonu Chinedum Endurance
# Team: TEAM-358-GROUP-A
# Description: FASGD-III (Facial Recognition Model)
# Country: Nigeria
# Date Created: 31-August-2020  "Buhari Regime"
# Date Modified:

# Importing the necessary modules
import os
import cv2
import pickle
import numpy as np
import imutils
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Setting the path to the dataset and model directory
embeddings = os.path.sep.join(["FASGDIII_facial_recognition", "models/embeddings.pickle"])
detector_model = os.path.sep.join(["FASGDIII_facial_recognition", "models/face_detection_model"])
embedding_model = os.path.sep.join(["FASGDIII_facial_recognition", "models/embeddingModel.t7"])
recognize_model = os.path.sep.join(["FASGDIII_facial_recognition", "models/output/recognizer.pickle"])
label_model = os.path.sep.join(["FASGDIII_facial_recognition", "models/output/le.pickle"])
X_encoder = os.path.sep.join(["FASGDIII_facial_recognition", "models/output/encoder.h5"])

# Setting the confidence value
confidence_value = 0.75


# Creating a class for facial recognition prediction
class FacialPrediction:
    def __init__(self, input_image):
        # Grabbing the input image
        self.frame = input_image

        # Loading the serialized face detector model into memory
        proto_path = os.path.join(detector_model, "deploy.prototxt")
        model_path = os.path.join(detector_model, "res10.caffemodel")

        # Creating the detector
        self.detector = cv2.dnn.readNetFromCaffe(proto_path, model_path)

        # Loading the actual face recognition model along with the label encoder
        self.model = pickle.loads(open(recognize_model, 'rb').read())

        # Loading the serialized face embedding model from disk
        self.embedder = cv2.dnn.readNetFromTorch(embedding_model)

        # loading the actual face recognition model along with the label encoder
        self.lb = pickle.loads(open(label_model, "rb").read())
        self.encoder = pickle.loads(open(X_encoder, "rb").read())

    # Making predictions
    def make_predictions(self):
        # Resizing the frame input to have a width of 600px
        self.frame = imutils.resize(self.frame, width=600)

        # loading the vide frame, resize it to have a width of 600 pixels and then
        # Grab its spatial dimensions
        (h, w) = self.frame.shape[:2]

        # Construct a blob from the image
        image_blob = cv2.dnn.blobFromImage(cv2.resize(self.frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0),
                                                    swapRB=False, crop=False)

        # Applying the opencv deep learning face detector to localize the faces in the image
        self.detector.setInput(image_blob)
        detections = self.detector.forward()

        # Setting the value for the predicted name to hold an unknown value at first
        pred_name = "null"

        # Creating the loop to loop over the detections and make predictions on the image
        # Also extract the confidence associated with the prediction
        # Filter out weak detections.
        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            # If / else block
            if confidence >= confidence_value:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                # Converting the values for box as integer values
                (startX, startY, endX, endY) = box.astype('int')

                # Extracting the face ROI
                face = self.frame[startY:endY, startX:endX]
                (fH, fW) = face.shape[:2]

                # Ensure the face width and height are sufficiently large
                if fW < 20 or fH < 20:
                    continue

                # Construct a blob for the ROI, then pass the blob through our face embedding model to
                # Obtain the 128-d quantification to the face.
                face_blob = cv2.dnn.blobFromImage(face, 1.0 / 255, (96, 96), (0, 0, 0),
                                                        swapRB=True, crop=False)

                # Making the predictions by converting the input image into numpy array and scaling down
                self.embedder.setInput(face_blob)
                vector = self.embedder.forward()

                # Making the actual prediction
                prediction = self.model.predict_proba(vector)[0]

                # Finding the actual name of the value predicted
                result = np.argmax(prediction)
                proba_val = prediction[result]
                name = self.lb.classes_[result]

                # Draw the bounding box of the face alond with the associated probability
                pred_name = "{}: {:.3f}".format(name, proba_val)
                y = startY - 10 if startY - 10 > 10 else startX + 10
                # Drawing the rectangle around the face
                cv2.rectangle(self.frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

                # Placing the predicted text
                # cv2.putText(self.frame, pred_name, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

        # Returning the frame
        return self.frame, pred_name
