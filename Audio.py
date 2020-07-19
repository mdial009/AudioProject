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


warnings.filterwarnings("ignore")


from twilio.rest import Client
'''
# put your own credentials here
account_sid = "ACcd77168694bb63deeeab6201c2696d20"
auth_token = "d4f5ec02f97d12a3d037d295df4b7c93"
client = Client(account_sid, auth_token)
client.messages.create(
    to="+13472847072",
    from_="+15864964098",
    body="Tomorrow's forecast in Financial District, San Francisco is Clear",
    media_url="https://climacons.herokuapp.com/clear.png")
'''
# A fuction thats going to records audio and return it as a string
def recordAudio():

    # Record the audio
    r = sr.Recognizer()  # Creating a recognizer object

    # Open the microphone and start recording
    with sr.Microphone() as source:
        while True:
            audio = r.listen(source)
            print(r.recognize_sphinx(audio))
        #r.adjust_for_ambient_noise(source) 
        #print("Say Something!")
        #audio = r.listen(source)
recordAudio()
    
'''
    # Use Google Speech Recognition
    # Created a empty string calling it data for Google Text-to-Speech to put the recorded audio into.
    data = " "
    # Using a try block to take that audio that was recorded and have Google Text-to-Speech output it as a string(data)
    try:
        data = r.recognize_google(audio)
        print("You Said: " + data)
    except sr.UnknownValueError:  # Checks for a unknown errors
        print("Google Speech Recognition Could Not Understand You")
    except sr.RequestError as e:
        print("Request Results From Google Speech Recognition Service Error" + e)

    return data

def wakeWord(text):
    WAKE_WORDS = ["now arriving at", "Hey Madani", "hey madani", "gonna dispense itself","Numbani","Nepal"]  # A list of Wake Words

    text = (
        text.lower() or text.capitalize()
    )  # Converting The Text To All Lower Case Words

    # Check To See If The Users Command/Text Contains A Wake Word/Phrase
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    # If The Wake Word isn't Found In The Text From The Loop And So It Returns False
    return False


while True:
    # Record The Audio
    text = recordAudio()

    # Check For The Wake Word/Phrase
    if wakeWord(text) == True:
        account_sid = "ACcd77168694bb63deeeab6201c2696d20"
        auth_token = "fcdeb038d8b45d077f71b65db7e63b3c"
        client = Client(account_sid, auth_token)
        client.messages.create(
        to="+13472847072",
        from_="+15864964098",
        body="You Are In A Game.",
        media_url="https://climacons.herokuapp.com/clear.png")
        sys.exit()
'''