from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
from Body.Listen import Listen
print(">> Starting The Friday : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Started The Friday : Wait For Few Seconds More")
from Main import MainTaskExecution
from Features.Music import Music
from Features.News import latestnews
from Features.time import Time
from Features.weather import Temp
from Features.Note import Notepad
from Features.Note import CloseNotepad
import requests
import bs4 as BeautifulSoup
def MainExecution():
    Speak("Hii")
    Speak("I'm Friday, I'm Ready To Assist You Sir.")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:
            pass
        elif "music " in Data:
            Music(Data)
        elif "time" in Data:
            Time(Data)
        elif "weather" in Data:
            weat()
        elif "news" in Data:
            latestnews()
        elif "note" in Data:
            Notepad()
        elif "close note" in Data:
            CloseNotepad()
        
            

        elif "whatsapp message" in Data:
            pass

        elif "turn on the tv" in Data:# Specific COmmand
            Speak("Ok..Turning On The Android TV")

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)
'''
def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        MainExecution()
    else:
        pass

ClapDetect()
'''
def weat():
         search= "temperature in bangalore"
         url=f"https://www.google.com/search?q={search}"
         r= requests.get(url)
         ans=BeautifulSoup(r.text,"html.parser")
         temperature=ans.find("div",class_="BNeawe").text
         Speak(f"the Temperature outside is {temperature} celcius")

MainExecution()


