#!/usr/bin/env python3

# Author: Mbonu Chinedum

# Importing the necessary packages
import os
import re
import io
import pickle
import string
import numpy as np
import random as rd
from gtts import gTTS
from time import sleep
from pygame import mixer
import speech_recognition as sr
from scipy.io.wavfile import read, write
from tensorflow.keras.models import Sequential
from .sound_recognition import SoundPrediction
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.layers import Dense, Activation, Dropout

# Setting the dimensions
INPUT_DIM = 1784
OUTPUT_DIM = 7

# Building the model
model = Sequential()
model.add(Dense(250, input_dim=INPUT_DIM, activation='relu'))
model.add(Dense(120, kernel_initializer='he_uniform', bias_initializer='zeros', activation='relu' ))
model.add(Dense(8, kernel_initializer='he_uniform', bias_initializer='zeros', activation='relu' ))
model.add(Dense(OUTPUT_DIM, activation='sigmoid'))

# Compile the model
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Getting the full path to the working dir
FULL_PATH = os.getcwd()

# Getting the full path for the serialized model and encoders directory
MODEL_FULL_PATH = os.path.sep.join([FULL_PATH, 'FASGDIII_soundwave_recogntion/model'])
ENCODERS_FULL_PATH = os.path.sep.join([FULL_PATH, "FASGDIII_soundwave_recogntion/encoders"])

# Getting the full path to the serialized model and encoder model weight file
MODEL_FILE = os.path.sep.join([MODEL_FULL_PATH, "fasgd-model.h5"])
ENCODER_MODEL_FILE = os.path.sep.join([ENCODERS_FULL_PATH, "encoders.pkl"])

# loading the pre-trained model into memory
model.load_weights(MODEL_FILE)

# loading the vectorizer model into memory
(VECTORIZER, LABEL_ENCODER) = pickle.load(open(ENCODER_MODEL_FILE, "rb"))

# Creating an instance of the recognizer class
r = sr.Recognizer()


# Creating a function for speaking
def google_speech(message):
    # Getting the path to the working directory.
    _FULL_PATH = os.getcwd()
    tts = gTTS(message, lang="en-us")
    tts.save("voice/message.mp3")

    # Load the popular external library
    mixer.init()
    mixer.music.load('voice/message.mp3')
    mixer.music.play()
    sleep(4)


# Creating a class for running the interactions
class Interaction:
    def __init__(self):
        # Creating a regex method for removing all the unwanted tags
        self.TAG_RE = re.compile(r'<[^>]+>')
        self.new_string = string.punctuation.replace(",", "")

        # Creating a list of unwanted words
        self.unwanted_words = ['please', 'define', 'what', 'who', 'whois',
                               'where is', 'tell me', 'what is', 'what',
                               'describe', 'explain', 'explain the following',
                               'describe ']

    # Creating a function for all the respective responses for the predicted
    # Labels.
    def responses(self, label):
        replies = {
            "age": ["I am one month old.", "One month older", "fasgd is one month old okay", "Just one month old",
                    "One month old, happy now i guess."],

            "goodbye": ["Sad to see you go", "Bye bye", "Okay then, goodbye"],

            "greetings": ["Hello", "Hi", "Hi, how are you", "Hello, how are you today", "Hello, how all is well"],

            "name": ["My name is fasgd, and it stands for facial acoustic, sound wave and gesture detection.", "Call me fasgd.",
                     "My name is fasgd. facial-acoustic sound and gesture detection.", "Call me fasgd for short okay."],

            "password": ["Sorry, I can't recognize your voice.", "Unable to recognize your voice"],

            "chinedu": ["Chinedu Voice Confirmed", "Hello Chinedu, your voice is confirmed."],

            "task": ["""Well, i am a security application that uses ML algorithms to perform facial recognition,
                        gesture recognition and sound wave recognition scan.""",
                     """ I am a security application that utilizes machine learning algorithms for verification
                     and authentication. I am mostly specialized in facial recognition, sound wave and gesture detection."""],

            "unknown": ["Sorry i do not understand you.", "Please speak again, i did not get that."]

        }

        # Returning the responses
        return rd.choice(replies[label])

    # Creating a function for using the regex parser
    def remove_tags(self, message):
        return self.TAG_RE.sub('', message)

    # Creating a function to clean the input tweets
    def clean_text(self, message):
        # Converting into small letters
        message = message.lower()
        # Removing unwanted tags
        message = self.remove_tags(message)
        # Remove the single character
        message = re.sub(r"\s+[a-zA-Z]\s+", ' ', message)
        # Removing the multiple spaces
        message = re.sub(r'\s+', ' ', message)
        # Removing the punctuation
        message = ''.join([words for words in message if words not in self.new_string])

        # Returning the filtered message
        return message

    # Creating a function for chatting
    def chat(self, message, wav_data):
        # Getting the user input message and performing some preprocessing
        # Functions on it by removing unwanted character and cleaning up
        clean_message = [self.clean_text(message)]

        # Making predictions but firstly transforming the clean text into
        # Vectors for easy predictions
        message_vectors = VECTORIZER.transform(clean_message).toarray()

        # PREDICTIONS
        PRED = model.predict(message_vectors)
        PRED = LABEL_ENCODER.classes_[np.argmax(PRED)]
        print(PRED)

        # SETTING THE VOICE RECOGNITION AUTHENTICATION PREDICTED VALUE AS False
        AUTH = False

        # Checking if the predicted label was password
        if PRED == "password":
            # Converting the extracted audio byte data into a wave format
            sr, data = read(io.BytesIO(wav_data))

            # Creating the byte object class and writing the extracted sound wave file
            # to the byte object as bytes.
            bytes_wav = bytes()
            byte_io = io.BytesIO(bytes_wav)
            write(byte_io, sr, data)            # Writing as a byte-type data

            # Saving the byte-type data as a wav file
            output_wav = byte_io.read()

            # Getting the full path to the wav file, then save.
            WAV_FILE = os.path.sep.join([FULL_PATH, 'voice/input_voice.wav'])
            # Saving the audio data as a wave file format
            with open(WAV_FILE, "wb") as wave_file:
                wave_file.write(output_wav)
                wave_file.close()

            # Creating an instance of the sound prediction class by passing the full
            # Path to the saved wav file format.
            SOUND_PREDICTION_CLASS = SoundPrediction(WAV_FILE)

            # Making prediction on the INPUT VOICE DATA
            SOUND_PREDICTION = SOUND_PREDICTION_CLASS.make_prediction()
            os.remove("voice/input_voice.wav")
            print(SOUND_PREDICTION)

            # IF predicted voice is chinedu, execute the code block below.
            if SOUND_PREDICTION == "chinedu":
                AUTH = True
                RESPONSE = self.responses("chinedu")

            # If predicted voice is not chinedu execute the code block below
            else:
                RESPONSE = self.responses(PRED)

            # Returning the final values and verified authentication
            return RESPONSE, AUTH

        # If the PRED value is not password, execute the code below.
        else:
            # Getting the response
            RESPONSE = self.responses(PRED)

            # Returning the predicted value
            return RESPONSE, AUTH



    # Creating a function for running the main interaction function
    def MainInteraction(self):
        while True:
            # Setting a try and exception rule here.
            try:
                # Reading audio data from the mic
                with sr.Microphone() as source:
                    print("Bee-A: Say something!!!")
                    # Removing background noise
                    r.adjust_for_ambient_noise(source)
                    # Recording the input sound wave data by listening.
                    audio = r.listen(source)
                    print("Bee-A: Recognizing..")
                    # Converting the audio data into textual data
                    msg = r.recognize_google(audio)

                # Getting the predicted values for the textual data and audio
                wav_data = audio.get_wav_data()
                message, AUTH = self.chat(msg, wav_data)


                # Displaying the message
                print(f"Bee-A: {message}")
                google_speech(message)

            # Exception rule if the conditions are not met.
            except:
                sleep(2)
                continue







        #     # Creating a function for running the main interaction function
        # def MainInteraction(self):
        #     while True:
        #         with sr.Microphone() as source:
        #             print("Bee-A: Say something!!!")
        #             # Removing background noise
        #             r.adjust_for_ambient_noise(source)
        #             # Recording the input sound wave data by listening.
        #             audio = r.listen(source)
        #             print("Bee-A: Recognizing..")
        #             # Converting the audio data into textual data
        #             msg = r.recognize_google(audio)
        #
        #         # Getting the predicted values for the textual data and audio
        #         wav_data = audio.get_wav_data()
        #         message, AUTH = self.chat(msg, wav_data)
        #
        #         # Displaying the message
        #         print(f"Bee-A: {message}")
        #         google_speech(message)
