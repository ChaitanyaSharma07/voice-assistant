from main import get_audio, speak
import json
import time
import os
from datetime import datetime
from datetime import date

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

