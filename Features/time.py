from Body.Speak import Speak
import datetime
from Body.Listen import MicExecution
def Time(Query):
    Query = str(Query).lower()

    if "time" in Query:
       strTime = datetime.datetime.now().strftime("%H:%M:%S")    
       Speak(f"Sir, the time is {strTime}")