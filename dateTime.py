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

    speak(day)
    speak(tdate)
    speak(month)
    speak(year)

tell_time()
tell_date()


