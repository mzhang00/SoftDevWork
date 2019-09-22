#Michael Zhang
#SoftDev1 pd1
#K8 -- First Flask app
#2019-09-18

from flask import Flask

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when run route requested
def hello_word():
    print(__name__) #where will this go? the console aka the terminal
    return "Hello World!"

@app.route("/spanish") #assign following fxn to run when run route requested
def hola_word():
    print(__name__) #where will this go? the console aka the terminal
    return "Hola Worldo!"

@app.route("/mandarin") #assign following fxn to run when run route requested
def nihao_word():
    print(__name__) #where will this go? the console aka the terminal
    return "Ni hao world!"

if __name__ == "__main__":
    app.debug = True #When this is false, the website no longer able to update authomatically when you make a change in the code
    app.run() #If this is commented out, the webstie is just not hosted
