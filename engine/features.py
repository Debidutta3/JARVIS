from playsound import playsound
import eel

@eel.expose #helps us to acces this function in main.js
#Play assistant sound function
def playAssistantSound():
    music_dir1 = "www\\assets\\audio\\shortStartVoice.mp3"
    playsound(music_dir1)
    

@eel.expose #helps us to acces this function in main.js
def playMicSound():
    music_dir2 = "www\\assets\\audio\\shortStartVoiceMic.mp3"
    playsound(music_dir2)