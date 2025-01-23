import speech_recognition as sr
import webbrowser as br
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS


r = sr.Recognizer()


def voice_recording(prompt = False):
    with sr.Microphone() as source:
        if prompt:
            anaxis_speak(prompt)
        print("listening ....")
        try:
            voice_data = ''
            audio = r.listen(source)      # Capture audio from the microphone
            voice_data = r.recognize_google(audio)
            # print("You said:", voice_data)
            return voice_data.lower()
        except sr.UnknownValueError:
            anaxis_speak("Sorry, I couldn't understand the audio.")
            return""
        except sr.RequestError as e:
            anaxis_speak(f"Could not request results from Bing Speech Recognition service; {e}")
            return ""
    
    
def anaxis_speak(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    r = random.randint(1,100000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print("Anaxix :",audio_string)   
    os.remove(audio_file)


def respond(voice_data):
    
    if 'your name' in voice_data :
        anaxis_speak(" my name is anaxis")

    if 'time' in voice_data :
        anaxis_speak(f"The time is {ctime()}.")
   
    elif 'search' in voice_data:
        search_query = voice_recording('what do you want to search for ?')
        if search_query:
            url = f"https://google.com/search?q={search_query}"
            br.open(url)
            anaxis_speak(f"Here are the search results for {search_query}.")
        else:
            anaxis_speak("I didn't catch that. Please try again.")
  
    elif 'location' in  voice_data:
        location_query = voice_recording('what location are you looking for ?')
        if location_query:
            url = 'https://google.nl/maps/place/'+ location_query+'/&amp;'
            br.get().open(url)
            anaxis_speak(f"Here is the location: {location_query}.")
        else:
            anaxis_speak("I couldn't get the location. Please try again.")

    elif 'exit' in voice_data:
        anaxis_speak("Goodbye! See you later.")
        exit()
    else:
        anaxis_speak("I'm not sure how to help with that.")

        
#main script 
time.sleep(1)
anaxis_speak("How can I help you today?")
while True:
    voice_data = voice_recording()
    if voice_data:
        respond(voice_data)





