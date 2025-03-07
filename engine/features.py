import re
from playsound import playsound
import os
import eel
from engine.config import ASSISTANT_NAME
from engine.command import speak
import pywhatkit as kit


@eel.expose #helps us to acces this function in main.js
#Play assistant sound function
def playAssistantSound():
    music_dir1 = "www\\assets\\audio\\shortStartVoice.mp3"
    playsound(music_dir1)
    

@eel.expose #helps us to acces this function in main.js
def playMicSound():
    music_dir2 = "www\\assets\\audio\\shortStartVoiceMic.mp3"
    playsound(music_dir2)
    

#function to open application file based on user's voice command
def openCommand(query):
    query = query.replace(ASSISTANT_NAME,"")
    query = query.replace("open", "")
    query.lower()
    
    if query!="":
        speak("Opening "+query)
        os.system('start '+query) #uses commands from cmd to open applications like start notepad
    else:
        speak("Sorry, I didn't get that.")
        
def playYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on Youtube")
    kit.playonyt(search_term)

#    
def extract_yt_term(command):
    #define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'   #\s+(.*?)\s+: dynamic term like play baawe on youtube
    
    #use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    
    #if match found then return the extracted song name; otherwise return none
    return match.group(1) if match else None