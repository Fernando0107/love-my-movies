import http.client
from flask import Flask, render_template, jsonify, redirect
import yaml
import os

developer = os.getenv("DEVELOPER", "User")
environment = os.getenv("ENVIRONMENT", "development")

app = Flask(__name__)


conn = http.client.HTTPSConnection("api.themoviedb.org")

payload = "{}"

conn.request("GET", "/3/configuration?api_key=12217434ad2932f49fc3abd52e259e8a", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

@app.route('/')                                         #Es la ruta "home"
def index():

    return render_template("bio.html")


if __name__ == '__main__':

  app.run(host="0.0.0.0", debug=True)
