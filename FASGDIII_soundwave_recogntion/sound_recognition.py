#!/usr/bin/env python3

# Author: Mbonu Chinedum Endurance
# Team: TEAM-358-GROUP-A
# Description: FASGD-III (Sound Wave Recognition)
# Country: Nigeria
# Date Created: 4th-September-2020  "Buhari Regime"
# Date Modified: 13th-sep-2020  "Buhari Regime"


# Importing the necessary modules
import os
import librosa
import numpy as np
import soundfile as sf
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dense, Dropout


# Creating a class for sound wave detection prediction
class SoundPrediction:
    def __init__(self, sound_wave):
        # Setting the output and input dimensions
        self.input_dim = (40, )
        self.output_dim = 2

        # Getting the input sound wave
        self.sound_wave = sound_wave

        # Setting path to the serialized model weight file
        self.model_path = os.path.sep.join(["FASGDIII_soundwave_recogntion", "model/voice_recognition.h5"])

        # loading the encoders
        self.encoders = os.path.sep.join(["FASGDIII_soundwave_recogntion", "encoders/label_encoder.npy"])

    # Creating a method for extracting the input sound wave features
    def extract_features(self):
        # Reading the input sound wave only when the wav name is not None
        if self.sound_wave:
            # Reading the sound wave data and its sample rate values
            X, sr = librosa.load(self.sound_wave, res_type="kaiser_fast")

        # Extracting features from the sound wave data and converting it into a numpy array.
        sound_data = librosa.feature.mfcc(y=X, sr=sr, n_mfcc=40)
        sound_data = np.mean(sound_data.T, axis=0)

        # Returning the scaled data
        return sound_data

    # Building the model
    def sound_model(self):
        # Creating an instance of the sequential model by adding 250 neurons.
        model = Sequential()
        model.add(Dense(250, input_shape=self.input_dim , activation="relu"))
        model.add(Dropout(0.1))

        # Adding another hidden layer with 128 neurons and a dropout layer of 0.5
        model.add(Dense(128, activation="relu"))
        model.add(Dropout(0.5))

        # Adding a last layer to the model
        model.add(Dense(self.output_dim, activation="sigmoid"))

        # Compiling the model
        model.compile(loss="binary_crossentropy", metrics=["accuracy"], optimizer="adam")

        # Returning the compiled model
        return model

    # Loading the serialized model from the specified path
    def make_prediction(self):
        # Creating an instance of the sound model
        loaded_model = self.sound_model()

        # Loading the model
        loaded_model.load_weights(self.model_path)

        # Loading the encoders
        (scaler, lb) = np.load(self.encoders, allow_pickle=True)

        # loading the sound wav for analysis
        sound_data = self.extract_features()

        # Reshaping the data
        sound_data = sound_data.reshape(1, -1)

        # Scaling down the data with the serialized encoder
        sound_data = scaler.transform(sound_data)

        # Making predictions
        predictions = np.argmax(loaded_model.predict(sound_data))
        predictions = lb.classes_[predictions]

        # Return the predictions
        return predictions
