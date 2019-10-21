import http.client
from flask import Flask, render_template, jsonify, redirect, json
import yaml
import os
import requests, sys
from key import key

stdout = sys.stdout

developer = os.getenv("DEVELOPER", "User")
environment = os.getenv("ENVIRONMENT", "development")

app = Flask(__name__)

movie_title = []
movie_overview = []
movie_source = []

alm = ["spiderman", "Goal", "joker", "Samurai", "avatar", "hacker", "gladiator"]

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

    movie_title.append(name)
    movie_overview.append(overview)
    movie_source.append(src)

    w = "http://image.tmdb.org/t/p/w92"+z

    Picture_request = requests.get(w)
    if Picture_request.status_code == 200:
        with open("./static/img/"+movie+".jpg", 'wb') as f:
            f.write(Picture_request.content)


for i in range(len(alm)):
    search_image(alm, alm[i],conn)


@app.route('/')                                         #Es la ruta "home"
def index():
    
    return render_template("home.html", movie = movie_title, src=movie_source, overview=movie_overview)


movie = "the flash"

@app.route('/search')  # Es la ruta "home"
def test():

    x = render_template("brain.html", movie=movie)


    return x

if __name__ == '__main__':

  app.run(host="0.0.0.0", debug=True)
