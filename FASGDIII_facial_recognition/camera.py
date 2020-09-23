#!/usr/bin/env python3

# Author: Mbonu Chinedum Endurance
# Team: TEAM-358-GROUP-A
# Description: FASGD-III (Facial Recognition Model)
# Country: Nigeria
# Date Created: 31-August-2020  "Buhari Regime"
# Date Modified:

# Importing the necessary modules
import os
import numpy as np
import pickle
import cv2
import imutils
from imutils import paths
from sklearn.svm import SVC
from imutils.video import VideoStream
from imutils.video import FPS
from sklearn.preprocessing import LabelEncoder, StandardScaler


# Setting the path to the dataset and model directory
img_dir = "dataset"
embeddings = "models/embeddings.pickle"
detector_model = "models/face_detection_model"
embedding_model = "models/embeddingModel.t7"
recognize_model = "models/output/recognizer.pickle"
label_model = "models/output/le.pickle"
X_encoder = "models/output/encoder.h5"

# Setting the confidence value
confidence_value = 0.75

# Define a video capture object
vs = cv2.VideoCapture(0)

# Loading the serialized face detector model into memory
proto_path = os.path.join(detector_model, "deploy.prototxt")
model_path = os.path.join(detector_model, "res10.caffemodel")

# Creating the detector
detector = cv2.dnn.readNetFromCaffe(proto_path, model_path)

# Loading the actual face recognition model along with the label encoder
model = pickle.loads(open(recognize_model, 'rb').read())

# Loading the serialized face embedding model from disk
embedder = cv2.dnn.readNetFromTorch(embedding_model)

# Loading the actual face recognition model along with the label encoder
lb = pickle.loads(open(label_model, "rb").read())
#encoder = pickle.loads(open(X_encoder, "rb").read())

# Setting some parameters
running = True;

# Running the while loop
while running:
    # Capture the video frame
    ret, frame = vs.read()
    frame = imutils.resize(frame, width=600)

    # Loading the video frame, resize it to have a width of 600 pixels and then
    # Grab its spartial dimensions
    (h, w) = frame.shape[:2]

    # Consttruct a blob from the  image
    imageBlob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300),
                                    (104.0, 177.0, 123.0), swapRB=False, crop=False)

    # Applying the opencv deep learning face detector to localize the faces in the images
    detector.setInput(imageBlob)
    detections = detector.forward()

    # Creating the loop to loop over the detections and make predictions on the image
    # Also extract the confidece associated with the prediction
    # Filter out weak detections.
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        #
        if confidence >= confidence_value:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            # Converting the values for box as integer values
            (startX, startY, endX, endY) = box.astype('int')

            # Extracting the face ROI
            face = frame[startY:endY, startX:endX]
            (fH, fW) = face.shape[:2]

            # Ensure the face width and height are sufficiently large
            if fW < 20 or fH < 20:
                continue
            # Construct a blob for the face ROI, then pass the blob through our face embdedding model to
            # Obtain the 128-d quantification to the face.
            face_blob = cv2.dnn.blobFromImage(face, 1.0 / 255, (96, 96),
                                             (0, 0, 0), swapRB=True, crop=False)

            # Making the predictions by converting the input image into numpy array and scaling down.
            embedder.setInput(face_blob)
            vector = embedder.forward()

            # performing predictions
            prediction = model.predict_proba(vector)[0]

            # Finding the name for the predicted value
            result = np.argmax(prediction)
            proba_val = prediction[result]
            name = lb.classes_[result]

            # Draw the bounding box of the face along with the associated probability.
            pred_name = '{}: {:.3f}'.format(name, proba_val)
            y = startY - 10 if startY - 10 > 10 else startX + 10
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)

            # Placing the predicted text
            cv2.putText(frame, pred_name, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow("Frame", frame)

    #
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
camera.release()
# Destroy all the windows
cv2.destroyAllWindows()
