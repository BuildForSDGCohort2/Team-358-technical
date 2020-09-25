#!/usr/bin/env python3

# Author: Mbonu Chinedum Endurance
# Team: TEAM-358-GROUP-A
# Description: FASGD-III (Main Server)
# Program: ANDELA BUILD FOR SDG COHORT-2 2020
# Country: Nigeria
# Date Created: 27-August-2020 "Buhari Regime"
# Date Modified:


# Importing the necessary modules
import os
import nltk
import pickle
import numpy as np
import random as rd
from gtts import gTTS
from time import sleep
import time
import imutils
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import email
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from collections import Counter
import cv2
import speech_recognition as sr
from datetime import datetime, timedelta
from FASGDIII_soundwave_recogntion.sound_recognition import SoundPrediction
from FASGDIII_facial_recognition.facial_recognition import FacialPrediction
from FASGDIII_gesture_recognition.gesture_recognition import GesturePredict


# Creating an instance of the recognizer class
r = sr.Recognizer()

# Setting the name of the video file
video_filename = "analyzed_video.avi"
frames_per_second = 24.0


# Creating a function to execute the sound model
def ExecSoundModel():
    pass


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


# Creating a function for sending video mails
def send_email(VIDEO_FILE):
    # Setting the subject email body
    SUBJECT = "SOMEONE DETECTED !!!"
    BODY = "Someone was detected, and the frames are below. Click to watch."
    SENDER_EMAIL = "noreplayalansmith@gmail.com"
    RECEIVER_EMAIL = "cboy.chinedu@gmail.com"
    PASSWORD = ""

    # Create a multipart message and set the headers
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL
    message["Subject"] = SUBJECT
    message["Bcc"] = RECEIVER_EMAIL

    # Adding the body of the email to the mime-multipart class
    message.attach(MIMEText(BODY, "plain"))

    # Adding the video file attachment
    filename = VIDEO_FILE

    # Loading teh file into memory as a read byte file
    with open(filename, "rb") as file:
        # Add the file as an application/octet-stream
        part = MIMEBase("application", "octet-stream")
        part.set_payload(file.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename = {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Logging into the server using secure context and send the email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)


# Creating a class for the main function
class MainFunction:
    def __init__(self):

        # Creating the first function to yield each captured frames as
        # a value returned back from the function
        self.running = True

    def record_frame(self, _value=0):
        cap = cv2.VideoCapture(2)

        # Define the codec and create VideoWriter object
        # fourcc = cv2.cv.CV_FOURCC(*'DIVX')
        # out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
        # Setting the filename
        filename = f"output{_value}.avi"
        out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'MJPG'), 19, (640, 480))

        font = cv2.FONT_HERSHEY_SIMPLEX
        count = 0

        while (cap.isOpened()):
            if count == 80:
                break

            ret, pred_frame = cap.read()
            #if ret is True:

            pred_frame = cv2.flip(pred_frame, 1)
            # Adding time stamp to the frames
            date_timestamp = str(datetime.now())
            (frame, pred_name, startX, startY, endX, endY) = FacialPrediction(pred_frame).make_predictions()

            if (startX is None) or (startY is None) or (endX is None) or (endY is None):
                cv2.putText(pred_frame, pred_name, (9, 25), font, 0.72, (0, 255, 0), 2)
                cv2.putText(pred_frame, date_timestamp, (9, 83), font, 0.72, (0, 255, 0), 2)

            else:
                # Drawing the segmented hand
                cv2.rectangle(pred_frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                cv2.putText(pred_frame, pred_name, (9, 25), font, 0.72, (0, 255, 0), 2)
                cv2.putText(pred_frame, date_timestamp, (9, 83), font, 0.72, (0, 255, 0), 2)

            # write the flipped frame
            out.write(pred_frame)

            #
            count += 1

        # Release everything if job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()

        # Returning the name of the saved video file
        return filename

    # Creating the function for performing the facial recognition.
    def Recognition(self):
        predicted_names = list()
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

        #
        saving_count = 0

        # Setting the time interval for recording the web frames to be 15 minutes
        estimated_time = datetime.now() + timedelta(minutes=5)

        # While looping
        while self.running:
            # Reading the frames
            ret, frame = vs.read()

            # Performing the facial recognition
            (frame, pred_name, startX, startY, endX, endY) = FacialPrediction(frame).make_predictions()

            # flip the frame so that it is not the mirror view
            frame = cv2.flip(frame, 1)

            # Clone the frame
            clone = frame.copy()

            result_names = pred_name.split(":")[0]

            # IF AN UNKNOWN PERSON IS DETECTED HERE, SEND NOTIFICATIONS TO THE
            # MOBILE APPLICATION AND SEND EMAIL NOTIFICATION AS WELL.
            # Appending the predicted names into the predicted_names list
            predicted_names.append(result_names)

            # FIND THE MOST PREDICTED NAME IN THE LIST
            if saving_count == 50:
                # Find the most occurred predicted names in the predicted_names list
                most_occured = Counter(predicted_names).most_common()
                # Extracting the values
                most_occured = most_occured[0][0]
                print(most_occured)
                #
                if most_occured == "person":
                    # SEND A NOTIFICATION TO THE MOBILE APPLICATION AND AN EMAIL
                    print("Unknown person detected.")

                    # Record the frames for 50 counts
                    VIDEO_FILE = self.record_frame(saving_count)
                    print(VIDEO_FILE)
                    send_email(VIDEO_FILE)
                    saving_count = 0

                    # SEND THE RECORDED SAVED FRAMES TO THE MOBILE APPLICATION OR ONLINE SERVER
                    # USING A POST REQUEST OR SOCKET.
                else:
                    saving_count = 0

            else:
                pass

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

            # Adding time stamp to the frames
            date_timestamp = str(datetime.now())
            cv2.putText(clone, date_timestamp, (9, 83), font, 0.72, (0, 255, 0), 2)

            # Drawing the segmented hand
            cv2.rectangle(clone, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(clone, result, (9, 25), font, 0.72, (0, 255, 0), 2)
            cv2.putText(clone, pred_name, (9, 51), font, 0.72, (0, 255, 0), 2)



            # cv2.imshow("Image", clone)
            # # cv2.waitKey(0)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break

            # Increasing the values for the number of frames by one
            num_frames += 1

            #
            saving_count += 1

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
        cv2.destroyAllWindows()

    # Creating the function for performing the facial recognition.
    def SecondCamera(self):
        # Capturing the video frames from the webcam.
        """
        Note that we can include ip-cameras into OPENCV which would be able
        To Grab frames from IOT web cameras for analysis.
        Here, we are using the frames captured from the webcam hosted or connected
        to the server. THANKS......
        """
        vs = cv2.VideoCapture(2)

        # Initialize the weight for running average
        aWeight = 0.5

        # Getting the region of interest (ROI) co-ordinates
        top, right, bottom, left = 8, 473, 221, 791  # y1, x1, y2, x2

        # Initialize the number of frames to be a zero value
        num_frames = 0

        # Setting the time interval for recording the web frames to be 15 minutes
        estimated_time = datetime.now() + timedelta(minutes=5)

        # While looping
        while self.running:
            # Reading the frames
            ret, frame = vs.read()

            # Performing the facial recognition
            (frame, pred_name, startX, startY, endX, endY) = FacialPrediction(frame).make_predictions()

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
            # if num_frames < 40:
            #     GesturePredict(gray).run_avg(aWeight)
            #
            # else:
            #     # Segment the hand region
            #     hand = GesturePredict(gray).segment()
            #     # Checking if the hand region is segmented
            #     if hand is not None:
            #         # if YES, UNPACK the thresholded image and segment the region
            #         (thresholded, segmented) = hand
            #
            #         # Draw the segmented region and display the frame
            #         cv2.drawContours(clone, [segmented + (right, top)], -1, (0, 0, 255))
            #
            #         # Making predictions
            #         result = GesturePredict(gray).make_predictions(thresholded)
            #
            #         #
            #         if num_frames == 200:
            #             num_frames = 0

            # Adding time stamp to the frames
            date_timestamp = str(datetime.now())
            cv2.putText(clone, date_timestamp, (9, 83), font, 0.72, (0, 255, 0), 2)

            # Drawing the segmented hand
            cv2.rectangle(clone, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(clone, result, (9, 25), font, 0.72, (0, 255, 0), 2)
            cv2.putText(clone, pred_name, (9, 51), font, 0.72, (0, 255, 0), 2)

            # cv2.imshow("Image", clone)
            # # cv2.waitKey(0)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break

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
        cv2.destroyAllWindows()

