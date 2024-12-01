from email.message import EmailMessage
import smtplib

import requests
import wikipedia
import pywhatkit as kit

EMAIL= "dkdhanush1970@gmail.com"
PASSWORD= ""
def find_my_ip():
    ip_address = requests.get('https://api.ipify.org?format=json').json()
    return  ip_address['ip']

def search_on_google(query):
    kit.search(query)

def youtube(video):
    kit.playonyt(video)

def search_on_wikipedia(query):
    results = wikipedia.summary(query,sentences=2)
    return results

def send_email(receiver_add, subject, message, false=False):
    try:
        email = EmailMessage()
        email['To']=receiver_add
        email['subject']=subject
        email['From']=EMAIL

        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.login(EMAIL,PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return false

def get_news():
    news_headline = []
    result = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey"
                          f"=df05b56d9aff42739fd270413d8208a6").json()
    articles = result["articles"]
    for article in articles:
        news_headline.append(article["title"])
    return news_headline[:6]

def weather_forecast(city):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?id={city}&appid"
                       f"=82be8135462d6ad2884eb5aadfae8087&units=metric").json()
    weather = res["weather"][0]["main"]
    temp = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temp}°C", f"{feels_like}°C"