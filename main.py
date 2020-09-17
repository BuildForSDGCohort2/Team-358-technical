#!/usr/bin/env python3

# Author: Mbonu Chinedum Endurance
# Team: TEAM-358-GROUP-A
# Description: FASGD-III (Main Server)
# Program: ANDELA BUILD FOR SDG COHORT-2 2020
# Country: Nigeria
# Date Created: 27-August-2020 "Buhari Regime"
# Date Modified:


# Importing the necessary modules
import cv2
import time
import imutils
from FASGDIII_facial_recognition.facial_recognition import FacialPrediction
from FASGDIII_gesture_recognition.gesture_recognition import GesturePredict


# Creating a common class
def make_face_prediction(input_image):
    # Loading the image into memory
    image = cv2.imread(input_image)
    # Passing the saved image into the prediction module
    (single_frame, pred_value) = FacialPrediction(image).make_predictions()
    # Placing the predicted value inside the image for just a single image.
    cv2.putText(single_frame, pred_value, (9, 51), cv2.FONT_HERSHEY_SIMPLEX, 0.72, (0, 255, 0), 2)
    # Saving the image to disk
    cv2.imwrite("Predicted.jpg", single_frame)


# Creating a class for the main function
class MainFunction:
    def __init__(self):
        # Creating the first function to yield each captured frames as
        # a value returned back from the function
        self.running = True

    # Creating the function for performing the facial recognition.
    def Recognition(self):
        # Capturing the video frames from the webcam.
        """
        Note that we can include ip-cameras into OPENCV which would be able
        To Grab frames from IOT web cameras for analysis.
        Here, we are using the frames captured from the webcam hosted or connected
        to the server. THANKS......
        """
        vs = cv2.VideoCapture(0)
        # Initialize the weight for running average
        aWeight = 0.5

        # Getting the region of interest (ROI) co-ordinates
        top, right, bottom, left = 8, 473, 221, 791  # y1, x1, y2, x2

        # Initialize the number of frames to be a zero value
        num_frames = 0

        # While looping
        while self.running:
            # Reading the frames
            ret, frame = vs.read()
            time.sleep(0.05)

            # Performing the facial recognition
            (frame, pred_name) = FacialPrediction(frame).make_predictions()

            # Checking is a None value was returned
            if pred_name.split(":")[0] == "unknown":
                print(pred_name)
                # Alert,,,, an unknown face has been detected...
                pass

            # Checking if the prediction is chinedu
            if pred_name.split(":")[0] == "chinedu":
                saved_clone = frame.copy()
                cv2.putText(saved_clone, pred_name, (9, 51),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.72, (0, 255, 0), 2)
                cv2.imwrite("predicted.jpg", saved_clone)
                pass

            # Resize the frame
            frame = imutils.resize(frame, width=800)

            # flip the frame so that it is not the mirror view
            frame = cv2.flip(frame, 1)

            # Clone the frame
            clone = frame.copy()

            # Get the height and width of the frame
            (height, width) = frame.shape[:2]

            # Get the ROI
            roi = frame[top:bottom, right:left]

            # Convert the roi to grayscale and blur it
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (7, 7), 0)

            # Setting the font
            font = cv2.FONT_HERSHEY_SIMPLEX
            result = "null"

            # To get the background, keep looking till a threshold is reached
            # So that our running average model gets calibrated
            if num_frames < 40:
                GesturePredict(gray).run_avg(aWeight)


            else:
                # Segment the hand region
                hand = GesturePredict(gray).segment()
                # Checking if the hand region is segmented
                if hand is not None:
                    # if YES, UNPACK the thresholded image and segment the region
                    (thresholded, segmented) = hand

                    # Draw the segmented region and display the frame
                    cv2.drawContours(clone, [segmented + (right, top)], -1, (0, 0, 255))

                    # Making predictions
                    result = GesturePredict(gray).make_predictions(thresholded)
                    #
                    if num_frames == 200:
                        num_frames = 0

            # Drawing the segmented hand
            cv2.rectangle(clone, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(clone, result, (9, 25), font, 0.72, (0, 255, 0), 2)
            cv2.putText(clone, pred_name, (9, 51), font, 0.72, (0, 255, 0), 2)

            # cv2.imshow("Image", clone)
            # cv2.waitKey(0)

            # Increasing the values for the number of frames by one
            num_frames += 1

            # Using puttext method for inserting text on video
            # cv2.putText(frame, "Hello Chinedum", (9, 25), font, 0.72, (0, 0, 255), 2)
            """
            The frames used here would be parsed into functions or classes which would
            perform analysis on the frames to give us the predicted values before encoding
            and sending/ yielding it out to the webserver for browser viewing. Thanks!!!!!!
            """
            # Saving each captured frame to disk as an image file
            ret, jpeg = cv2.imencode(".jpg", clone)
            img = jpeg.tobytes()

            # Sending back each frame captured back as a returned value for the
            # Created function
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n\r\n')

        # Closing and cleaning up
        vs.release()
        vs.close()