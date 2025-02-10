import pyttsx3
import speech_recognition as sr

#function to enable speak feature
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    print(voices)
    engine.say(text) #speak the given text
    engine.runAndWait() #wait when there is space or punctuation marks
    

def takeCommand():
    r = sr.Recognizer() #Recognizer is a class to recognize speech
    
    with sr.Microphone() as source: #using microphone as source audio
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #recognize the audio and the language is english india
        print(f"User said: {query}\n")
    except Exception as e:
        return ""
    
    return query.lower() #return the output in lowercase

text = takeCommand() #call the function to take the input
speak(text) #output of the taken input