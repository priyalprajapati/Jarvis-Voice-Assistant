
# Jarvis-Voice-Assistant

A Python-based voice-activated assistant (Jarvis) that can recognize voice commands, speak responses, and perform tasks like web browsing, playing music, telling the time, and more!




## Features

- Listen to voice commands using speech recognition
- Speak responses using text-to-speech (pyttsx3
- Open YouTube or Google
- Perform Google searches for custom queries
- Tell the current time
- Tell a joke
- Play random music from your specified folder
- Gracefully exit when commanded


## Installation

1. Clone the Repository:

```bash
git clone https://github.com/priyalprajapati/Jarvis-Voice-Assistant.git
cd Jarvis-Voice-Assistant
```
2. Install Dependencies:
    
 ```bash
pip install -r requirements.txt
pip install pipwin
pipwin install pyaudio
```
3. Configure Your Music Folder:
- Open jarvis.py.
- Replace the music folder path:
```bash
music_dir = "E:\\Music"  # Change to your actual music folder path
```




## Usage
Run the assistant:
```bash
python jarvis.py
```


## Supported Voice Commands

- "open youtube" → Opens YouTube
- "open google" → Opens Google
- "search for [query]" → Searches Google for your query
- "what is your name" → Tells Jarvis's name
- "what time is it" → Tells the current time
- "tell me a joke" → Tells a programming joke
- "play music" → Plays a random song from your specified folder
- "exit" or "quit" → Exits Jarvis




##  Dependencies
- pyttsx3
- speechrecognition
- pyaudio (installed via pipwin)
- webbrowser
- datetime
- os, random
## License

This project is licensed under the MIT License.




## Note
- Ensure you have a working microphone and internet connection for voice recognition.
- Update the music folder path (E:\\Music) to your actual music directory on your system.
