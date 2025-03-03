import os
import eel

from engine.features import *
from engine.command import *

#in which folder, index.html is present
eel.init("www")

playAssistantSound()

#output will be shown in the localhost 8000
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

#start the program
eel.start('index.html', mode=None, host='localhost', block=True)