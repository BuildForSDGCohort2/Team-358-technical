#!/usr/bin/env python3

# Author: Mbonu Chinedum Endurance
# Team: TEAM-358-GROUP-A
# Description: FASGD-III (Main Server)
# Program: ANDELA BUILD FOR SDG COHORT-2 2020
# Country: Nigeria
# Date Created: 27-August-2020 "Buhari Regime"
# Date Modified:


# Importing the necessary modules
from main import MainFunction
from flask import Flask, render_template, jsonify, Response

# Creating the flask application
app = Flask(__name__)


# Creating an instance of the predicted live feed
live_feed = MainFunction()


# Creating the first Route
@app.route("/")
def index():
    # Streaming the video
    return render_template("index.html")


# Creating the second route for sending the Grabbed video frames on the
# Server and making it possible to view the frames
@app.route("/gesture_recognition_frames")
def gestureFeed():
    # Streaming the video live on the server
    return Response(live_feed.Recognition(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/gesture_recognition_frames/hands")
def gestureHands():
    # Streaming the gesture hands side by size with the main frame
    return "<h1> Hello Nedu </h1>"


# Creating the third route for the facial recogniton frames
@app.route("/facial_recognition_frames")
def facialFeed():
    pass


# Running the application
if __name__ == "__main__":
    app.run(debug=True)
