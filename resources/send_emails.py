#!/usr/bin/env python3

"""
This script is written to send emails to a mail
server.
it works mostly with GMAIL

"""

# Importing the necessary modules

# Importing the necessary modules
import os
import cv2
import ssl
import json
import smtplib
import requests
import cloudinary
import cloudinary.uploader
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from collections import Counter
import speech_recognition as sr
from datetime import datetime, timedelta
from key.encryption import Encryption
from FASGDIII_soundwave_recogntion.sound_recognition import SoundPrediction
from FASGDIII_facial_recognition.facial_recognition import FacialPrediction
# from FASGDIII_gesture_recognition.gesture_recognition import GesturePredict


# Creating a function for sending video mails
def send_email(VIDEO_FILE):
    # Setting the subject email body
    SUBJECT = "[ALERT] SOMEONE DETECTED !!!"
    BODY = """\
        <html>
            <head>
            <link href="https://fonts.googleapis.com/css2?family=David+Libre&display=swap" rel="stylesheet">

            <style>
                body{display: flex; align-content: center; justify-content: center; background-color: white;}
                p{margin-left: 16px;  font-size: 12px; color: black; font-family: 'David Libre', serif;}
                h2{margin-left: 10px; color: red; font-family: 'David Libre', serif; text-align: center; font-size: 40px;}
            </style>
            </head>

            <body>
                <center> <h2> ALERT !!! </h2> </center> <br>

                <p> <b> Hello </b>, <br>
                Someone was detected by camera two. <br>
                The recorded frames are below. <br>
                Click to watch.  </p>  <br>
            </body>
        </html>


    """
    SENDER_EMAIL = "fasgd.alert@gmail.com"
    RECEIVER_EMAIL = "cboy.chinedu@gmail.com"
    PASSWORD = decrpyted_keys.Decrypt()[0]

    # Create a multipart message and set the headers
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL
    message["Subject"] = SUBJECT
    message["Bcc"] = RECEIVER_EMAIL

    # Adding the body of the email to the mime-multipart class
    message.attach(MIMEText(BODY, "html"))

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

