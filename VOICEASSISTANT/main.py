from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import random
from datetime import datetime
from random import choice
import time
import webbrowser


r= sr.Recognizer()
def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice=''
        try:
            voice = r.recognize_google(audio,language='tr-TR')
        except sr.UnknownValueError:
            print('Anlayamadım .Tekrar eder misin?')
        except sr.RequestError:
            print("sistem üzgün sanırım çalışmıyor")
        return voice


def responce(voice):
   
        if "merhaba" in voice :
             speak("sana da merhaba en sevdiğim kişi")
        if "selam" in voice:
            speak("aleyküm selam ")
        if "teşekkür ederim" in voice or "teşekkürler" in voice :
            speak("rica ederim")
        if "görüşürüz" in voice :
            speak("görüşelim")       
            exit()
        if "hangi gündeyiz" in voice:
            today =time.strftime("%A")
            speak(today)
        if "saat kaç" in voice:
            selection =["hemen bakıyorum ", "saat şuan "]
            clock = datetime.now().strftime("%H:%M")
            selection = random.choice(selection)
            speak(selection+clock)
        if "google'da ara" in voice :
            speak("ne aramamı istersin")
            search= record()#bizden komut bekleyecek
            url = "https://www.google.com/search?q={}".format(search)
            webbrowser.get().open(url)
            speak("{} içi Google'da bulabildiklerimi listeliyorum.".format(search))



def speak(string):
    tts=gTTS(text=string ,lang='tr')#google'aa bağlanmamızı sağlayan köprü
    file='answer.mp3'
    tts.save(file)#ses kaydoldu
    playsound(file)#sesi çaldık
    os.remove(file)#sesi sildik 

def test(wake):
    if "katya" in wake:
        playsound("DING.mp3")
        wake = record()
        if wake != '':
            voice = wake.lower()
            print(wake.capitalize())
            responce(voice)


speak('hey')
playsound("DING.mp3")
#playsound("starting.mp3")
#sürekli arkada bizi dinlemesi için while 

    
while True:
    wake = record()
    if wake != '':
        wake = wake.lower()
        print(wake.capitalize())
        test(wake)








