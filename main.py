import speech_recognition as sr
import webbrowser as br
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS


r = sr.Recognizer()


def voice_recording(ask = False):
    with sr.Microphone() as source:
        if ask:
            anaxis_speak("what do you wanna search for")
        # print("listening ....")
        audio = r.listen(source)      # Capture audio from the microphone
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            # print("You said:", voice_data)

        except sr.UnknownValueError:
            anaxis_speak("Sorry, I couldn't understand the audio.")

        except sr.RequestError as e:
            anaxis_speak(f"Could not request results from Bing Speech Recognition service; {e}")
        return voice_data
    
    
def anaxis_speak(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    r = random.randint(1,100000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)   
    os.remove(audio_file)


def respond(voice_data):
  
    if 'what is your name' in voice_data :
        anaxis_speak(" my name is anaxis")

    if 'what time is it' in voice_data :
        anaxis_speak(ctime())
   
    if 'search' in voice_data:
        search = voice_recording('what do you want to search for ?')
        url = 'https://google.com/search?q='+search
        br.get().open(url)
        anaxis_speak("this is the results that i found about "+search)
  
    if 'location' in  voice_data:
        location = voice_recording('what is the location ?')
        url = 'https://google.nl/maps/place/'+ location+'/&amp;'
        br.get().open(url)
        anaxis_speak("here is yoou location")

    if 'exit' in voice_data:
        anaxis_speak("see you later")
        exit()

        
#main script 
time.sleep(1)
while(1):
    anaxis_speak("How can i help-")
    voice_data = voice_recording()
    respond(voice_data)





