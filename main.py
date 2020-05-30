import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            reply(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            reply('Sorry, I did not get that')
        except sr.RequestError:
            reply('Sorry, my speech service is down')  
        return voice_data  

def respond(voice_data):
    if 'what is your name' in voice_data:
        reply('My name is Jarvis')
    if 'what time is it' in voice_data:
        reply(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        reply('Here is what I found for ' + search)
        webbrowser.get().open(url)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        reply('Here is the location of ' + location)
        webbrowser.get().open(url)  
    if 'close' in voice_data:
        exit() 
    if 'tell a joke' in voice_data:
        i = random.randint(1, 5)
        joke(i)  
    if 'compose email' in voice_data:
        url = 'https://mail.google.com/mail/u/0/#inbox?compose=new'
        reply('Here you go!')
        webbrowser.get().open(url)
    if 'play music' in voice_data:
        i = random.randint(1, 5)
        playsound.playsound('./music/music' + str(i) + '.mp3')
    if 'start pomodoro' in voice_data:
        pomodoro()


def reply(audio_string):
    tts = gTTS(text = audio_string, lang = 'en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    print(audio_string)
    playsound.playsound(audio_file)
    os.remove(audio_file)

def joke(i):
    start_line = {1: "What is the king of all school supplies?", 2: "Why did the computer squeak?", 3: "What's the difference between you and a Calendar?", 4: "What has four legs and flies?", 5: "What type of investment do chemists prefer?"}
    punch_line = {1: "The Ruler", 2: "Someone stepped on it's mouse.", 3: "A Calendar has a date on Valentine's day.", 4:"A garbage truck!", 5: "They have an affinity for bonds."}
    reply(start_line[i])
    reply(punch_line[i])

def pomodoro():
    reply("Pomodoro started")
    n = 25 #Number of minutes for pomodoro
    for i in range(n):
        print(str(n-i) + ' minutes remaining.')
        time.sleep(60)
    reply("Done")
    
time.sleep(1)   
reply('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)




