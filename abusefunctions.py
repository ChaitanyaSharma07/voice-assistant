import random
import playsound
from gtts import gTTS  
curses = [
    "Do you know who my dad is? Why didn't your mom tell you?"
]

def speak(text):
    random_num = random.randint(1, 100)
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def abuse():
    random_curse = random.choice(curses)
    speak(random_curse)

