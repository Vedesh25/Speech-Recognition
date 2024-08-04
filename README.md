"# Speech-Recognition" 
This project is a simple virtual assistant built using Google Text-to-Speech (gTTS), SpeechRecognition, and other Python libraries. It listens to the user's voice commands, processes them, and performs various actions such as telling the time, opening Google, sending emails, and more.

Features
 - Voice Recognition: Listens to user commands using the speech_recognition library.
 - Text-to-Speech: Responds to user commands using Google's gTTS library.
 - Time Telling: Tells the current time.
 - Web Navigation: Opens Google or locates places on Google Maps.
 - Email Sending: Sends emails to predefined contacts.
 - Stop Command: Stops listening and responding to commands.

Dependencies
 - gtts: Google Text-to-Speech library
 - speech_recognition: Library for performing speech recognition
 - playsound: Library for playing sound files
 - smtplib: Library for sending emails
 - webbrowser: Library for opening web pages
 - pyaudio: Library for working with audio (required for speech_recognition)

Example Commands
 - "How are you"
 - "Time"
 - "Open Google"
 - "Locate [place]"
 - "Email"
 - "Stop"

Code Overview
 - listen()
    Listens for the user's voice command using the speech_recognition library and returns the transcribed text.

 - respond(String)
    Converts the given text to speech using gTTS and plays the audio.

 - virtual_assistant(data)
    Processes the user's voice command and performs actions such as telling the time, opening Google, locating places, sending emails, or stopping the assistant.
   
