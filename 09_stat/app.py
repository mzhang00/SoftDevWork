#Michael Zhang
#SoftDev1 pd1
#K9 - Second Flask app
#2019-09-20

from flask import Flask, render_template

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when run route requested
def hello_word():
    print(__name__) #where will this go? the console aka the terminal
    return "Hello World"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template") #assign following fxn to run when run route requested
def test_tmplt():
    return render_template('/model_tmplt.html', foo = "fooooo", collection = coll)

if __name__ == "__main__":
    app.debug = True #When this is false, the website no longer able to update authomatically when you make a change in the code
    app.run() #If this is commented out, the webstie is just not hosted
