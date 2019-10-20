import http.client
from flask import Flask, render_template, jsonify, redirect, json
import yaml
import os
from bs4 import BeautifulSoup
import requests, sys
from key import key

stdout = sys.stdout

developer = os.getenv("DEVELOPER", "User")
environment = os.getenv("ENVIRONMENT", "development")

app = Flask(__name__)

alm = ["spiderman", "Goal", "joker", "the dark knight", "avatar", "hacker", "gladiator"]

conn = http.client.HTTPSConnection("api.themoviedb.org")

def search_image(alm, movie, conn):

    payload = "{}"

    conn.request("GET", "/3/search/movie?api_key="+key+"&language=en-US&query="+ movie, payload)

    res = conn.getresponse()
    data = res.read()
    x = data.decode("utf-8")

    d = json.loads(x)


    z = d["results"][0]["poster_path"]
    w = "http://image.tmdb.org/t/p/w92"+z

    Picture_request = requests.get(w)
    if Picture_request.status_code == 200:
        with open("./static/img/"+movie+".jpg", 'wb') as f:
            f.write(Picture_request.content)


for i in range(len(alm)):
    search_image(alm, alm[i],conn)



'''
def json_Brain(x):
    try:
        # Get a file object with write permission.
        file_object = open("test.json", 'w+')

        # Save dict data into the JSON file.
        json_data = json.dump(x, file_object, indent=4, sort_keys=False)


        print("test.json" + " created. ")

    except FileNotFoundError:
        print("test.json" + " not found. ")


json_Brain(d)
'''

@app.route('/')                                         #Es la ruta "home"
def index():
    
    return render_template("home.html")


movie = "the flash"

@app.route('/search')  # Es la ruta "home"
def test():

    x = render_template("brain.html", movie=movie)


    return x

# ======================================================== Soup ==========================================================



if __name__ == '__main__':

  app.run(host="0.0.0.0", debug=True)
