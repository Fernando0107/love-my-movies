import http.client
from flask import Flask, render_template, jsonify, redirect, json
import yaml
import os
import requests, sys
from redis import Redis
from key import key
from var import *

stdout = sys.stdout

developer = os.getenv("DEVELOPER", "User")
environment = os.getenv("ENVIRONMENT", "development")

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

conn = http.client.HTTPSConnection("api.themoviedb.org")

def search_image(alm, movie, conn):

    payload = "{}"

    conn.request("GET", "/3/search/movie?api_key="+key+"&language=en-US&query="+ movie, payload)

    res = conn.getresponse()
    data = res.read()
    x = data.decode("utf-8")

    d = json.loads(x)


    z = d["results"][0]["poster_path"]
    name = d["results"][0]["original_title"]
    overview = d["results"][0]["overview"]
    src = "./static/img/"+movie+".jpg"
    date = d["results"][0]["release_date"]

    movie_title.append(name)
    movie_overview.append(overview)
    movie_source.append(src)
    movie_date.append(date)

    if movie in alm2:
        movie_title2.append(name)
        movie_overview2.append(overview)
        movie_source2.append(src)
        movie_date2.append(date)

    if movie in alm3:
        movie_title3.append(name)
        movie_overview3.append(overview)
        movie_source3.append(src)
        movie_date3.append(date)


    w = "http://image.tmdb.org/t/p/w92"+z

    Picture_request = requests.get(w)
    if Picture_request.status_code == 200:
        with open("./static/img/"+movie+".jpg", 'wb') as f:
            f.write(Picture_request.content)

for i in range(len(alm)):
    search_image(alm,alm[i],conn)


@app.route('/')                                         #Es la ruta "home"
def index():
    
    return render_template("home.html", movie=movie_title, src=movie_source, overview=movie_overview, date=movie_date, movie2=movie_title2, src2=movie_source2, overview2=movie_overview2, date2=movie_date2, movie3=movie_title3, src3=movie_source3, overview3=movie_overview3, date3=movie_date3)


movie = "the flash"

@app.route('/search')  # Es la ruta "home"
def test():

    x = render_template("brain.html", movie=movie)


    return x

if __name__ == '__main__':

  app.run(host="0.0.0.0", debug=True)
