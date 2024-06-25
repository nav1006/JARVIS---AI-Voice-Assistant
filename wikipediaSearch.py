import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def tell_time():
    Time = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak("the current time is")
    speak(Time)

def tell_date():
    tdate = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    day = datetime.datetime.now().strftime("%A")
    speak("the current date is")
    speak(tdate)
    speak(month)
    speak(year)
    speak(day)

def greet():
    hour = datetime.datetime.now().hour
    if hour >= 5 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Sir")
    elif hour >= 18 and hour < 24:
        speak("Good evening Sir")
    else:
        speak("Hello Sir, Its past Midnight!")

def wishme():
    speak("Welcome back sir!")
    greet()
    speak("Jarvis at your service sir!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Pardon me sir, Can you speak again")
        return "None"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            tell_time()
        elif 'date' in query:
            tell_date()
        elif 'wikipedia' in query:
            speak("Searching")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'offline' in query:
            speak("Going to sleep Sir")
            quit()