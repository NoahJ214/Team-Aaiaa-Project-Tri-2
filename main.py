# import "packages" from flask
import json


from crud.app_crud import app_crud
from flask import render_template, request, Flask
from __init__ import app
# create a Flask instance
app.register_blueprint(app_crud)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/timmy/')
def Timmy():
    return render_template("timothy.html")


@app.route('/ritvik/', methods=['GET', 'POST'])
def Ritvik():
    return render_template("ritvik.html")



@app.route('/nathan/')
def Nathan():
    return render_template("nathan.html")

@app.route('/william/')
def William():
    return render_template("william.html")

@app.route('/noah/')
def Noah():
    return render_template("noah.html")

@app.route('/ballquiz')
def basketballquiz():
    return render_template("basketballquiz.html")

@app.route('/ballgame')
def basketballgame():
    return render_template("basketballgame.html")

@app.route('/jeopardy')
def jeopardy():
    return render_template("jeopardy.html")
# @app.route('/basketball/', methods=['GET', 'POST'])
# def basketball():
#   url = "http://localhost:5000/api/basketball_api"
#   response = requests.request("GET", url)
#   return render_template("ritvik.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(host='0.0.0.0' port=80, debug=True)