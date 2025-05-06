import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
import os
from openai import OpenAI
from dotenv import load_dotenv

recognizer= sr.Recognizer()
engine=pyttsx3.init()

def configure():
    load_dotenv()
    
def speak(text):
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


def aiprocess(command):
    
    headers = {
        "Authorization": f"Bearer {os.getenv('api_key')}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo", 
        "messages": [
            {
                "role": "system",
                "content": "You are a virtual assistant named AURA skilled in general tasks like Alexa and Google Cloud.Keep responses concise but informative."
            },
            {
                "role": "user",
                "content": command
            }
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open stack overflow" in c.lower():
        webbrowser.open("https://stackoverflow.com/")
    elif "play music" in c.lower():
        webbrowser.open("https://open.spotify.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=music_library.music[song]
        webbrowser.open(link)


    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={os.getenv('newsapi')}")
        if r.status_code == 200:
            # parse the JSON response
            data = r.json()
            # Extract the articles
            articles = data.get("articles", [])
            # print the headlines
            for article in articles:
                speak(article['title'])

    else:
        # let OpenAI handle the request
        output=aiprocess(c)
        speak(output)


if __name__=="__main__":
    speak("Initializing AURA")
    while True:
        #Listen for the wake word "AURA"
        #obtain audio from the microphone
        r = sr.Recognizer() 
        
        # recognize speech using Google
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1) #listen Fn takes 2 parameters..."Timeout" & "phrase_time_limit"
            word=r.recognize_google(audio)
            if(word.lower()=="aura"):
                speak("Hello, how can I assist you?")

                    #listen for command
                with sr.Microphone() as source:
                    print("AURA Active...")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)

                    process_command(command)

        
        except Exception as e:
            print("Error;{0}".format(e))



