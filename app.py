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
from flask import Flask, render_template, Response, redirect, url_for

# Creating the flask application
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z##!!-+=/'

# Creating an instance of the predicted live feed
live_feed = MainFunction()


# Creating the first Route
@app.route("/")
def index():
    return render_template("index.html")


# Create a route for recording the frames
@app.route('/record_frames')
def record_frames():
    live_feed.record_frame()
    return redirect(url_for('second_camera'))


# Creating the second route for sending the Grabbed video frames on the
# Server and making it possible to view the frames
@app.route("/gesture_recognition_frames", methods=["POST", "GET"])
def gestureFeed():
    # Streaming the video live on the server
    return Response(live_feed.Recognition(),
                        mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/second_camera")
def second_camera():
    # load the image
    return Response(live_feed.SecondCamera(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


# Running the application
if __name__ == "__main__":
    app.run(debug=True)












# image = cv2.imread("static/images/predicted0.jpg")
#
# # Passing the image into the predicted class
# (pred_image, pred_value) = FacialPrediction(image).make_predictions()
#
# # Saving the predicted image and its value to disk
# # Putting the predicted text into the frame
# cv2.putText(pred_image, pred_value, (9, 51), cv2.FONT_HERSHEY_SIMPLEX,
#                                         0.72, (0, 255, 0), 2)
#
# # Writing the predicted image to disk
# cv2.imwrite("static/images/pred_image.jpg", pred_image)
#
# # Streaming the gesture hands side by size with the main frame
# #return redirect(url_for('facialFeed'))
# return render_template("predicted_value.html", pred_value=pred_value)