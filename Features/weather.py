import requests
from Body.Speak import Speak
import bs4 as BeautifulSoup
from Body.Listen import MicExecution

def Temp():
         search= "temperature in bangalore"
         url=f"https://www.google.com/search?q={search}"
         r= requests.get(url)
         ans=BeautifulSoup(r.text,"html.parser")
         temperature=ans.find("div",class_="BNeawe").text
         Speak(f"the Temperature outside is {temperature} celcius")
       
    
