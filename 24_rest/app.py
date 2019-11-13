from flask import Flask, render_template
import urllib.request, json
from json import loads
from urllib.request import urlopen

app = Flask(__name__)

@app.route("/")
def root():
    u = urllib.request.urlopen(
    "https://api.nasa.gov/planetary/apod?api_key=NHZYuhe3G4IYQftAt1abs1rltUwNxwVaj8YUCenb"
    )
    response = u.read()
    data = json.loads( response )
    return render_template("index.html", pic = data['url'], desc = data['explanation'])

if  __name__ == '__main__':
    app.debug = True
    app.run()
