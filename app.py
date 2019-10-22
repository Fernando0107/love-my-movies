import http.client
from flask import Flask, render_template, jsonify, redirect, json
import requests, sys, os, yaml
import redis
from key import key
from var import *


developer = os.getenv("DEVELOPER", "User")
environment = os.getenv("ENVIRONMENT", "development")

app = Flask(__name__)
#redis = Redis(host='redis', port=6379)
r_server = redis.Redis("localhost")

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
    vote = d["results"][0]["vote_count"]

    movie_title.append(name)
    movie_overview.append(overview)
    movie_source.append(src)
    movie_date.append(date)
    movie_vote.append(vote)

    #r_server.rpush("movies", name)

    if movie in alm2:
        movie_title2.append(name)
        movie_overview2.append(overview)
        movie_source2.append(src)
        movie_date2.append(date)
        movie_vote2.append(vote)

    if movie in alm3:
        movie_title3.append(name)
        movie_overview3.append(overview)
        movie_source3.append(src)
        movie_date3.append(date)
        movie_vote3.append(vote)


    w = "http://image.tmdb.org/t/p/w92"+z

    Picture_request = requests.get(w)
    if Picture_request.status_code == 200:
        with open("./static/img/"+movie+".jpg", 'wb') as f:
            f.write(Picture_request.content)

for i in range(len(alm)):
    search_image(alm,alm[i],conn)

def cache_request(conn, request, callback):

    if not can_cache(conn, request):
        return callback(request)

    page_key = 'cache:'+ hash_request(request)

    content = conn.get(page_key)

    if not content:

        content = callback(request)

        conn.setex(page_key, content, 300)

    return content



@app.route('/')                                         #Es la ruta "home"
def index():
    
    return render_template("home.html", movie=movie_title, src=movie_source, overview=movie_overview, date=movie_date, movie2=movie_title2, src2=movie_source2, overview2=movie_overview2, date2=movie_date2, movie3=movie_title3, src3=movie_source3, overview3=movie_overview3, date3=movie_date3, vote=movie_vote, vote2=movie_vote2, vote3=movie_vote3)


movie = "the flash"

@app.route('/search')  #Solo para referencia
def test():

    x = render_template("brain.html", movie=movie)


    return x

if __name__ == '__main__':

    test = True
    app.run(host="0.0.0.0", debug=True)
