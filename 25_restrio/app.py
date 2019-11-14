from flask import Flask, render_template
import urllib.request, json
from json import loads
from urllib.request import urlopen
import random

app = Flask(__name__)

@app.route("/")
def root():
    u = urllib.request.urlopen(
    "https://rickandmortyapi.com/api/character/"
    )
    response = u.read()
    data = json.loads( response )
    randomint = random.randint(0,17)
    return render_template("index.html", pic = data['results'][randomint]['image'], name = data['results'][randomint]['name'])

@app.route("/TylerMFN1")
def tyler1():
    res = urlopen(
        "https://en.wikipedia.org/w/api.php?format=json&action=query&formatversion=2&prop=pageimages%7Cpageterms&titles=Tyler1"
    ).read()

    data = json.loads(res)
    return render_template("tyler1.html", tylerData=data["query"]["pages"][0]["terms"]["alias"][0])

if  __name__ == '__main__':
    app.debug = True
    app.run()
