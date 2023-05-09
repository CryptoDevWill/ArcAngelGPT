import os
import tempfile
from gtts import gTTS
from playsound import playsound
from utils.load_settings import load_settings

mute_speech = load_settings.mute_speech

def speak(text):
    if mute_speech:
        return
    
    tts = gTTS(text=text, lang='en')
    
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        temp_file = f"{fp.name}.mp3"
        tts.save(temp_file)
        playsound(temp_file)
        os.remove(temp_file)

def mute_button(mute):
    global mute_speech
    mute_speech = mute