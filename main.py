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

#authorisation function will ask for
def authorization():
    steps = []

    #getting password
    speak("please tell the password")
    password = get_audio()

    real_password = "password"

    if password == real_password:
        steps.append(True)
        speak("Please look at the camera for facial recognition of user")
        time.sleep(3)
        random_num = random.randint(0, 100)

        video_capture_object = cv2.VideoCapture(0)

        ret, frame = video_capture_object.read()
        img_name = "Face" + str(random_num) + ".jpg"
        cv2.imwrite(img_name, frame)

        video_capture_object.release()
        cv2.destroyAllWindows()


        #confirming faces
        known_image = face_recognition.load_image_file("pic1.jpg")
        unknown_image = face_recognition.load_image_file(img_name)

        my_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([my_encoding], unknown_encoding)
        print(results)

        if results:
            steps.append(True)

            speak("Please enter the password into the command prompt")

            the_password = "coding"
            password_inp = input("Enter password: ")

            if password_inp == the_password:
                run = True
            else:
                run = False
                speak("incorrect password, shutting down")
        else:
          speak("Unauthorized user, shutting down")

    else:
        speak("incorrect password, shutting down")

def make_folder():
    speak("Please tell the folder name")
    folder_name = get_audio()
    time.sleep(2)
    os.mkdir(folder_name)
    
    action = "folder by the name of " + str(folder_name) + " was made"

    now  = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    today = date.today()
    the_date = today.strftime("%m/%d/%y")

    dataset= {
        "action": action,
        "time": current_time,
        "date": the_date
    }

    with open("archive.json", 'r+') as file:
        data = json.load(file)
        data["archive"].append(dataset)
        file.seek(0)
        json.dump(data, file, indent=4)

def read_file():
    speak("Please tell me the file name")
    file_name = get_audio()

    for i in os.listdir():
        name = os.path.splitext()[0]
        ext = os.path.splitext()[1]

        if name == file_name and (ext == (".txt" or ".docx")): 
            with open(file_name, 'r+') as file:
                speak(file.read())

def make_file():
    speak("Please tell me the file name with extension")
    file_data = get_audio()

    file_details = file_data.split(".")

    file_name = str(file_details[0])  + "." + str(file_details[1])

    opener = open(file_name)

    action = "file by the name of " + str(file_name) + " was made"

    now  = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    today = date.today()
    the_date = today.strftime("%m/%d/%y")

    dataset= {
        "action": action,
        "time": current_time,
        "date": the_date
    }

    with open("archive.json", 'r+') as file:
        data = json.load(file)
        data["archive"].append(dataset)
        file.seek(0)


while run:
    command = get_audio()

    if (("create" or "make") and ("folder" or "directory")) and not("do not" or "don't" or "no") in command:
        make_folder()
    elif (("read" or "tell me") and ("file")) and not("do not" or "don't" or "no") in command:
        read_file()
    elif (("create" or "make") and "file") and not("do not" or "don't" or "no") in command:
        make_file()

authorization()