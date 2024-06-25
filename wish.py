import pyttsx3
import datetime

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def tell_time():
    Time = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak(Time)

def tell_date():
    tdate = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    day = datetime.datetime.now().strftime("%A")

    speak(tdate)
    speak(month)
    speak(year)
    speak(day)

def wishme():
    speak("Welcome back sir!")
    speak("the current time is")
    tell_time()
    speak("the current date is")
    tell_date()
    speak("Jarvis at your service sir!")

wishme()