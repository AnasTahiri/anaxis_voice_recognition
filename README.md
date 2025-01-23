# Anaxis Voice Assistant

Anaxis is a simple voice assistant that responds to your voice commands, searches the web, and provides basic functionalities like telling the time and finding locations.

## Features
- **Name Inquiry**: Ask the assistant its name.
- **Current Time**: Get the current system time.
- **Web Search**: Perform Google searches through voice commands.
- **Location Search**: Find locations on Google Maps.
- **Exit Command**: Safely exit the assistant.

## Requirements
This project is built with Python. Ensure you have the following dependencies installed:
- `SpeechRecognition`: For capturing and processing voice input.
- `gTTS`: To convert text to speech.
- `playsound`: To play audio files.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/anaxis-voice-assistant.git
   cd anaxis-voice-assistant

 2.  Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows

3.Install the dependencies:
  pip install -r requirements.txt


Usage
Run the script:

bash
Copy
Edit
python anaxis.py
Interact with the assistant using the following commands:

"What is your name?": Learn the assistant's name.
"What time is it?": Get the current time.
"Search [your query]": Perform a Google search.
"Location [place]": Find a location on Google Maps.
"Exit": Exit the program.

Notes
Ensure your microphone is connected and working.
The assistant requires an active internet connection for web searches and text-to-speech functionality.
Contributing
Feel free to fork this repository and submit pull requests. Suggestions and improvements are always welcome!

License
This project is licensed under the MIT License.


---

### Instructions for GitHub
1. Save the `requirements.txt` in the root directory of your project.
2. Save the `README.md` in the root directory of your project.
3. Push both files along with your code to your GitHub repository:
   ```bash
   git add requirements.txt README.md
   git commit -m "Add requirements and README files"
   git push origin main
