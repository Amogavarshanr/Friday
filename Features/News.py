import requests
import json
from Body.Speak import Speak


def latestnews():
    api_dict = {"business" :"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=a76c2ff251334571baf35bc6ce8312d8 ",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=a76c2ff251334571baf35bc6ce8312d8",#Enter Your OWN API ,
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=a76c2ff251334571baf35bc6ce8312d8",#Enter Your OWN API,
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=a76c2ff251334571baf35bc6ce8312d8",#Enter Your OWN API,
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=a76c2ff251334571baf35bc6ce8312d8",#Enter Your OWN API,
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=a76c2ff251334571baf35bc6ce8312d8"#Enter Your OWN API
}

    content = None
    url = None
    Speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    Speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        Speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    Speak("these were the top news")
