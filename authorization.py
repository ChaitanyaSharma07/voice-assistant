import cv2
import face_recognition
import random
import time
import main
import playsound
from gtts import gTTS
import speech_recognition as sr 

#authorisation function will ask for

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


def auth():
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
                main.run = False
                speak("incorrect password, shutting down")
        else:
          speak("Unauthorized user, shutting down")

    else:
        speak("incorrect password, shutting down")

auth()