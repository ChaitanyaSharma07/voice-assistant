from __future__ import print_function
import os
import time
import playsound
from face_recognition.api import face_encodings
import speech_recognition as sr
from gtts import gTTS                
import datetime
import os.path
from datetime import datetime
from datetime import date
import json
import cv2
import random
import face_recognition
from authorization import auth
import osfunctions
import browsing
global action
run = False
    
def speak(text):
    random_num = random.randint(1, 100)
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


#using sr module to get the audio from the microphone and then using it
def get_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)
        speech = ""

        try:
            speech = r.recognize_google(audio)
            print("you said " + str(speech))
        except Exception as e:
            print("Exception is: " + str(e))

    return speech



while run:
    command = get_audio()

    if (("create" or "make") and ("folder" or "directory")) and not("do not" or "don't" or "no") in command:
        osfunctions.make_folder()
    elif (("read" or "tell me") and ("file")) and not("do not" or "don't" or "no") in command:
       osfunctions.read_file()
    elif (("create" or "make") and "file") and not("do not" or "don't" or "no") in command:
       osfunctions.make_file()
    elif (("play" or "search") and "video") and not("do not" or "don't" or "no") in command:
        browsing.youtube()

auth()