from flask import Flask
from flask import render_template
from flask import request
from urllib.parse import quote, uses_query
from urllib.request import urlopen
import urllib.parse
import json

app = Flask(__name__)

newsurl = "https://newsapi.org/v2/everything?q={0}&apiKey=b5cbaa6a984d4dc7942dfb39c1a98c75"
covid19 = "http://newsapi.org/v2/top-headlines?country=th&q=%E0%B9%82%E0%B8%84%E0%B8%A7%E0%B8%B4%E0%B8%94&apiKey=b5cbaa6a984d4dc7942dfb39c1a98c75"
weatherurl = "http://api.openweathermap.org/data/2.5/weather?q={0}&units=metric&lang=th&appid=50c134e83f7476ad58997ae3ff0ef78b"
imgurl = "http://openweathermap.org/img/wn/{0}@2x.png"

@app.route("/")
def home():
    city = request.args.get("city")
    if not city:
        city = "Bangkok"
    query = quote(city) 
    url = weatherurl.format(query)
    data = urlopen(url).read()
    parsed = json.loads(data)
    desc = parsed["weather"][0]["description"]
    temp = parsed["main"]["temp"]
    pres= parsed["main"]["pressure"]
    hum = parsed["main"]["humidity"]
    wind = parsed["wind"]["speed"]
    name = parsed["name"]
    img = imgurl.format(parsed['weather'][0]['icon'])
    weath = {"desc" : desc,
            "temp":temp,
            "pres":pres,
            "hum":hum,
            "wind":wind,
            "img":img,
            "name":name}
    


    data = urlopen(covid19).read()
    parsed = json.loads(data)
    covid19news = []
    for i in range(0, 5):
        covid19news.append({"head":parsed['articles'][i]['title'], 
            "content":parsed['articles'][i]['description'], 
            "img":parsed['articles'][i]['urlToImage'], 
            "url":parsed['articles'][i]['url']})
    return render_template("home.html",news = covid19news,weather = weath )

@app.route("/search")
def search():
    news = request.args.get("news")
    if not news:
        return render_template("search.html",new = [0,])    
    query = quote(news) 
    url = newsurl.format(query)
    data = urlopen(url).read()
    parsed = json.loads(data)
    new = [len(parsed['articles'])]
    for i in range(len(parsed['articles'])):
        title = parsed["articles"][i]["title"]
        des = parsed["articles"][i]["description"]
        urlnews = parsed["articles"][i]["url"]
        new.append({"title":title,"des":des,"urlnews":urlnews})
    return render_template("search.html",new = new)


@app.route("/about")
def about():
    return render_template("about.html")

def convert_to_unicode(txt):
    encode = urllib.parse.quote(txt)     
    return encode

app.env="development"
app.run(debug=True,use_reloader=True)