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
    randomint = random.randint(0,20)
    return render_template("index.html", pic = data['results'][randomint]['image'], name = data['results'][randomint]['name'])

if  __name__ == '__main__':
    app.debug = True
    app.run()
