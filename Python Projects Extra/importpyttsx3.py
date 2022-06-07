import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

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
        speak(f"hello {tt} how are you? ")
    tt1 = takeCommand()
    if "not fine" or "Not Good" or "theek nahi hu" in query:
        speak("ohh.. You are Not GOOD.... WHAT Happened?.........tell me Please")
if __name__ == "__main__":
    wishMe()
    question()
