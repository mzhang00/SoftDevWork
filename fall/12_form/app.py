#Jesse Hall and Michael Zhang
#SoftDev1 pd1
#K12 -- Echo Echo Echo
#2019-09-26

from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def whyTho():
    return render_template('testforms.html')

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    #print('hello')
    #session['Username'] = request.args['username']
    #print(session.pop('Username'))
    #print(request.cookies.get('username'))
    return render_template('auth.html', user = request.args['username'], requestmethod = request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()
