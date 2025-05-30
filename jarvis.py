import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os
import random

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Optional: choose female voice
engine.setProperty('rate', 150)  # Speed of speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand the audio.")
        return ""
    except sr.RequestError:
        speak("Could not request results; check your internet connection.")
        return ""

def jarvis():
    speak("Hello, I am Jarvis, your assistant. How can I assist you today?")
    while True:
        command = listen()

        if "open youtube" in command:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")
        
        elif "open google" in command:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")
        
        elif "search for" in command:
            search_query = command.replace("search for", "")
            speak(f"Searching for {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        
        elif "what is your name" in command:
            speak("I am Jarvis, your personal assistant.")
        
        elif "what time is it" in command:
            now = datetime.datetime.now()
            speak(f"The time is {now.strftime('%I:%M %p')}")
        
        elif "tell me a joke" in command:
            speak("Why did the programmer quit his job? Because he didn't get arrays!")
        
        elif "play music" in command:
           speak("Playing a random song from your music folder.")
           music_dir = "E:\Music"  # Your music folder
           songs = os.listdir(music_dir)
           song_choice = random.choice(songs)
           os.startfile(os.path.join(music_dir, song_choice))

        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        
        elif command != "":
            speak("I'm sorry, I can't do that yet.")

if __name__ == "__main__":
    jarvis()
