import pyttsx3
import speech_recognition as sr
import eel
import time

#function to enable speak feature
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text) #display the spoken message
    engine.say(text) #speak the given text
    engine.runAndWait() #wait when there is space or punctuation marks
    
def takeCommand():
    r = sr.Recognizer() #Recognizer is a class to recognize speech
    
    with sr.Microphone() as source: #using microphone as source audio
        print("Listening...")
        eel.DisplayMessage("Listening...") #import the function from controller.js and Display listening by which we can display the
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)
    
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...") #After speaking, recognizing should come.
        query = r.recognize_google(audio, language='en-in') #recognize the audio and the language is english india
        print(f"User said: {query}\n")
        eel.DisplayMessage(query) #display the spoken message after listening.
    except Exception as e:
        return ""
    
    return query.lower() #return the output in lowercase

@eel.expose #Now we can access the takeCommand function in html
def allCommands():
    query = takeCommand()
    print (query)
    
    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
        
    elif "on youtube":
        from engine.features import playYoutube
        playYoutube(query)
        
    else:
        print("Not running..")
        
    eel.showHood()