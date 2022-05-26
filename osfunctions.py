import json
import time
import os
from datetime import date
from datetime import datetime
import random
from gtts import gTTS
import playsound
import speech_recognition as sr

def speak(text):
    random_num = random.randint(1, 100)
    tts = gTTS(text=text, lang="en")
    filename = "voice" + str(random_num) + ".mp3"
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

def archive(dataset):
    with open("archive.json", 'r+') as file:
        data = json.load(file)
        data["archive"].append(dataset)
        file.seek(0)

    

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

    data= {
        "action": action,
        "time": current_time,
        "date": the_date
    }

    archive(data)



def read_file():
    speak("Please tell me the file name")
    file_name = get_audio()

    for i in os.listdir():
        name = os.path.splitext()[0]
        ext = os.path.splitext()[1]

        if name == file_name and (ext == (".txt" or ".docx")): 
            with open(file_name, 'r+') as file:
                speak(file.read())

#------------------------------------------------------


def make_file():
    speak("Please tell me the file type: ")
    file_data = get_audio()

    extension = ""
    file_name = ""

    if "word" in file_data.lower():
        extension = "docx"
        speak("Please tell me the file name.")
        file_name = get_audio()

    elif "excel" in file_data.lower():
        extension = "xlsx"
        speak("Please tell me the file name.")
        file_name = get_audio()

    elif "json" in file_data.lower():
        extension = "json"
        speak("Please tell me the file name.")
        file_name = get_audio()

    elif "text" in file_data.lower():
        extension = "txt"
        speak("Please tell me the file name.")
        file_name = get_audio()

    file_name.replace(" ", "_")

    file_uri = file_name + "." + extension
    print("file: " + file_uri)

    opener = open(file_uri)

    action = "file by the name of " + str(file_uri) + " was made"

    now  = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    today = date.today()
    the_date = today.strftime("%m/%d/%y")

    data= {
        "action": action,
        "time": current_time,
        "date": the_date
    }

    archive(data)

make_file()