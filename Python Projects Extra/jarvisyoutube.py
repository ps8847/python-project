import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import time
import keyboard

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',100)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e: 
        print("Say that again please...")  
        return "None"    
    return query
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am a Robot made by Prince Sharma...... I CAN HELP YOU IN MANY WAYS...")       
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def question():
    speak("OKAY........................if you dont mind ,, can you tell me what is your name?")
    tt = takeCommand()

    tt=tt.replace("my","")
    tt=tt.replace("name","")
    tt=tt.replace("mera","")
    tt=tt.replace("naam","")
    tt=tt.replace("is","")
    if tt =="":
        exit()
    else:
        speak(f"hello {tt}.......how are you? ")
    tt_i = takeCommand()
    if tt_i = "":
        exit()
    if "not fine" or "Not Good" or "theek nahi hu" in query:
        speak("ohh.. You are Not GOOD.... WHAT Happened?.........tell me Please")
        tt2 = takeCommand()
        if "not feeling good" in tt2:
            speak("ohh,,, its feels so bad that You are not feeling good now")
            speak("Please tell me what i should do so that you can feel good")
            tt3 = takeCommand()
            if "play music" or "Play songs" in tt2:
                speak(f"ok. {tt} ..i will play songs for you........Tell me whcih song you want to listen")
                tt4 = takeCommand()
                if "Open youtube" or "youtube" or "youtube songs" in tt4:
                    webbrowser.open("youtube.com")
                    time.sleep(5)
                    speak(f"{tt}..you want to maximize the screen?")
                    tt5 = takeCommand()
                    if "no" or "not want" in tt5:
                        speak(f"ok , {tt} No problem")
                    if "yes" or "yes i" or "i want" in tt5:
                        speak(f"ok.. {tt}..screen is maximized now")
                    speak(f"I'm in Youtube {tt} ..now please tell me which song you want to listen now")
                    pyautogui.click(532,100)
                    tt6=takeCommand()
                    speak(f"okay {tt} what i found you want to search is :..... {tt6}...........if you want to search this....Say .YES .or .NO")
                    tt7=takeCommand()
                    for i in tt7:
                        if "repeat" or "yes repeat" in tt7:
                            speak(f"okay {tt} i will repeat it.....{tt6}")
                        if "no" in tt7:
                            speak("Okay....you want to search something else or it was wrong?")
    else:
        speak("yeah,, Great ..good to heir that you are great")
        speak("you wan")
    
if __name__ == "__main__":
    wishMe()
    question()
