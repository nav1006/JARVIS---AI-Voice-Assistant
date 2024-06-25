import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb

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


def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('10navdeepkumar@gmail.com', 'roos ijhr wsap erbw')
    server.sendmail('10navdeepkumar@gmail.com', to, content)
    server.close()


def chromeSearch():
    chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    speak("What should I search sir?")
    search = takeCommand().lower()
    wb.get(chromepath).open_new_tab(f"https://www.google.com/search?q={search}")


def playSongs():
    songs_dir = 'D:/JARVIS/songs'
    songs = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir, songs[0]))


def rememberThat():
    speak("What should I remember sir?")
    data = takeCommand()
    speak("you said me to remember that" + data)
    remember = open('remind.txt', 'w')
    remember.write(data)
    remember.close()


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
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'send email' in query or 'send an email' in query:
            try:
                speak("What should I send sir?")
                content = takeCommand()
                to = 'Harshit11042003@gmail.com'
                sendmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the mail")

        elif 'search in chrome' in query:
            chromeSearch()

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            speak("Playing your favourite song sir!")
            playSongs()

        elif 'remember that' in query:
            rememberThat()

        elif 'what did I ask you to remember' in query:
            remember = open('remind.txt','r')
            speak("you said me to remember that"+remember.read())

        elif 'offline' in query or 'sleep' in query:
            speak("Going to sleep Sir")
            quit()
