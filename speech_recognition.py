#Google Text To Speech

from gtts import gTTS #google text to speech
import speech_recognition as sr
import playsound
from time import ctime #Current-time
import os
import re #regex
import uuid #universal unique id
import smtplib
import webbrowser

#to make sure it listens
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Start talking")
        audio = r.listen(source,phrase_time_limit=5)
    data = ""
    #Exception Handling
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed") 
    return data
listen()

#To respond back with audio 
def respond(String):
    print(String)
    tts = gTTS(text = String,lang = 'en-US')
    tts.save("speech.mp3")
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

#Start giving actions
#Virtual Assistant actions
def virtual_assistant(data):
    """give your actions"""

    if "how are you" in data:
        listening = True
        respond("Good and doing well")

    if "time" in data:
        listening =True
        respond(ctime())


    if "open google" in data.casefold():
        listening = True
        url = "https://www.google.com/"
        webbrowser.open(url)
        respond("Success")

    if "locate" in data:
        webbrowser.open('https://www.google.com/maps/search/'+
                        data.replace("locate",""))
        result = "Located"
        respond("Located {}".format(data.replace("locate","")))

    if "email" in data:
        listening = True
        respond("Whom should i send email to?")
        to = listen().lower()
        edict = {'ved-1':'vedesh_kottapalli@srmap.edu.in','parthiv':'parthivgundubogula@gmail.com'} #give mail ids
        toaddr = edict[to]
        respond("What is the Subject?")
        subject = listen()
        respond("What should i tell that person?")
        message = listen()
        content = 'Subject :{}\n\n{}'.format(subject,message)

        #init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com',587)
        #identify the server
        mail.ehlo()
        mail.starttls()
        #login
        mail.login('vedesh.kot@gmail.com','eldtwuihkfyobera') #enter mailid and app password make sure you enable less secure app access
        mail.sendmail('vedesh.kot@gmail.com',toaddr,content) #enter your gmail username
        mail.close()
        respond('Email Sent')

    if "stop" in data:
        listening =False
        print("Listening Stopped")
        respond("Okay done take care...")

    try:
        return listening
    except UnboundLocalError:
        print("Timedout")
        
respond("Hey Vedesh how are you")
listening = True
while listening ==True:
    data = listen()
    listening = virtual_assistant(data)


