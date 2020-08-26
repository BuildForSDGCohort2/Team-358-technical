#!/usr/bin/env python3

# Author: Mbonu Chinedum Endurance
# Company: Facebook Andela
# TEAM:
# Date Created:


# Importing the necessary modules 
from flask import Flask, render_template, jsonify, Response
import imutils 
import cv2 

# Creating the flask application
app = Flask(__name__)

# Capturing the video frames from the webcam
""" Note that we can include ip-cameras into OPENCV which would be able
    To Grab frames from IOT web cameras for analysis. 
    Here, we are using the frames captured from the webcam hosted or connected 
    to the server. THANKS...... 
"""
vs = cv2.VideoCapture(0)

# Creating the first function to yield each captured frames as
# a value returned back from the function
running = True
def generateFrames():
    while running:
        # Reading the frames 
        ret, frame = vs.read()
        frame = imutils.resize(frame, width=800) 
        
        # Convert the image to grayscale, blur it, and find edges in
    # the image 
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # frame = cv2.bilateralFilter(frame, 11, 17, 17)
        # frame = cv2.Canny(frame, 30, 200)

        # frame = cv2.GaussianBlur(frame, (7, 7), 1)
        # frame = cv2.threshold(frame, 60, 255, cv2.THRESH_BINARY)[1]
        """
        The frames used here would be parsed into functions or classes which would 
        perfom analysis on the frames to give us the predicted values before encoding 
        and sending/ yielding it out to the webserver for brower viewing. Thanks!!!!!! 
        """
        # Saving each captured frame to disk as an image file
        ret, jpeg = cv2.imencode(".jpg", frame)
        img = jpeg.tobytes()

        # Sending back each frame captured back as a returned value for the
        # Created function
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +  img + b'\r\n\r\n')

    vs.release()

# Creating the first Route
@app.route("/")
def index():
    # Streaming the video
    return render_template("index.html")

# Creating the second route for sending the Grabbed video frames on the
# Server and making it possible to view the frames
@app.route("/video_feed")
def video_feed():
    # Streaming the video live on the server
    return Response(generateFrames(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


# Running the application
if __name__ == "__main__":
    app.run()
    



    


