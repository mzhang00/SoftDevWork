#Team Meseeks (Eric Lam and Michael Zhang)
#SoftDev1 pd1
#K15 -- Login Site
#2019-10-01

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
logged = False

@app.route("/", methods=['GET','POST'])
def rootFunc():
    if logged:
        return render_template('welcome.html')
    else:
        return render_template('login.html')

@app.route("/check")
def authenticate():
    # session['Username'] = request.args['username']
    # print(session.pop('Username'))
    # #print(request.cookies.get('username'))
    if request.args["username"] == "Michael" and request.args["password"] == "hunter2":
        return render_template('welcome.html', user=request.args["username"])
    else:
        user = request.args["username"] != "Michael"
        pword = request.args["password"] != "hunter2"
        error = 'Bad Juju' if user and pword else 'Bad Username' if user else 'Bad Password'
        return render_template("error.html", message=error)

if __name__ == "__main__":
    app.debug = True
    app.run()
