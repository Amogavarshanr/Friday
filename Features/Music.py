import pywhatkit
from Body.Speak import Speak
from Body.Listen import MicExecution
def Music(Query):
    Query = str(Query).lower()

    if "music" in Query:
        Speak("which song should i play sir!")
        musicname = MicExecution()
        pywhatkit.playonyt(musicname)
        