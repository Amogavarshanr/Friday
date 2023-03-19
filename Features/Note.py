from Body.Speak import Speak
from datetime import datetime
from Body.Listen import MicExecution
import os

def Notepad():

    Speak("Tell Me The Query .")
    Speak("I Am Ready To Write .")

    writes = MicExecution()

    time = datetime.now().strftime("%H:%M")

    filename = str(time).replace(":","-") + "-note.txt"

    with open(filename,"w") as file:

        file.write(writes)

    path_1 = "C:\ai_project\Features" + str(filename)

    path_2 = "C:\ai_project\DataBase\notepad" + str(filename)

   # os.rename(path_1,path_2)

    os.startfile(path_1)

def CloseNotepad():

    os.system("TASKKILL /F /im Notepad.exe")