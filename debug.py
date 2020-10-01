from FASGDIII_soundwave_recogntion.interact import Interaction
import time

res = Interaction()


res.MainInteraction()









#
# [ 'unknown']
# import librosa
# from scipy.io.wavfile import read, write
# import numpy as np
# import io
# import speech_recognition as sr
#
#
# r = sr.Recognizer()
#
#
#
# while True:
#     # Setting a try and exception rule here.
#     # Reading audio data from the mic
#     with sr.Microphone() as source:
#         print("Bee-A: Say something!!!")
#         # Removing background noise
#         r.adjust_for_ambient_noise(source)
#         # Recording the input sound wave data by listening.
#         audio = r.listen(source)
#
#         #
#         wav_data = audio.get_wav_data()
#
#     #
#     sr, data = read(io.BytesIO(wav_data))
#
#     #
#     bytes_wav = bytes()
#     byte_io = io.BytesIO(bytes_wav)
#     write(byte_io, sr, data)
#
#     #
#     output_wav = byte_io.read()
#     with open("voice/input_voice.wav", "wb") as f:
#         f.write(output_wav)
#         f.close()
#
#     # loading the wav voice into memory
#     X, sr = librosa.load("voice/input_voice.wav", res_type="kaiser_fast")
#
#     print(X)
#
#
#     # print(s)
#     # print(s.shape)
#     # print("Second Sr: ", rate)
#
#     #
#     # s = np.asarray(s)
#     # sound_data = np.mean(s.T, axis=0)
#     #
#     # print(sound_data)
#
#     exit()





