#!/usr/bin/env python3

"""
This application is built to send sms message using twilio application

"""

# Importing the necessary modules
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

# Setting the sms body and phone number
body = """
    Hello,
    Someone was detected on camera two. Open your mobile application to view the recorded frames,
    or click on this link to view it live.
    Link: https://youtu.be/kib6uXQsxBA

    """
twilio_number = ""
destination_number = ""

# Sending the messages
message = client.messages.create(
            body=body,
            from_=twilio_number,
            to=destination_number
        )

print(message.sid)
