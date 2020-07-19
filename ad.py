import pyaudio
import wave
import os
import speech_recognition as sr
import warnings
import sys
import sphinx
import pocketsphinx
from pocketsphinx import Pocketsphinx
from pocketsphinx import LiveSpeech, get_model_path

def voice_input():
    global a2t
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)
        r.record(source,duration=2)
        print("Say something!")
        audio = r.listen(source)
    try:
        a2t=r.recognize_sphinx(audio,keyword_entries=[('forward',1.0),('backward',1.0),('left',1.0),('right',1.0),('stop',1.0),('find line',0.95),('follow',1),('lights on',1),('lights off',1)])
        print("Sphinx thinks you said " + a2t)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    BtnVIN.config(fg=color_text,bg=color_btn)
    return a2t 
voice_input()