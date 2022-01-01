import urllib.request
import re
import webbrowser
import main
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
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


#getting our url
def youtube():
    speak("What would you like to search")
    input = get_audio()
    search = input.replace(" ","+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    main_url = "https://www.youtube.com/watch?v=" + video_ids[0]

    #opening the url
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(main_url)