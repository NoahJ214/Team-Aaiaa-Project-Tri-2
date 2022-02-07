# import "packages" from flask
import json

from Blueprints.profiles import profiles
from crud.app_crud import app_crud
from flask import render_template, request, Flask
from __init__ import app
# create a Flask instance
app.register_blueprint(app_crud)
app.register_blueprint(profiles)

# connects default URL to render sportsstore.html

from api.basketball import nba_api
app.register_blueprint(nba_api)


@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html

@app.route('/basketball/')
def basketball():
    return render_template("basketball.html")

@app.route('/football/')
def football():
    return render_template("football.html")

@app.route('/baseball/')
def baseball():
    return render_template("baseball.html")

@app.route('/tennis/')
def tennis():
    return render_template("tennis.html")

@app.route('/ballquiz')
def basketballquiz():
    return render_template("basketballquiz.html")


@app.route('/ballgame')
def basketballgame():
    return render_template("basketballgame.html")

@app.route('/sportsstore')
def sportsstore():
    return render_template("sportsstore.html")

@app.route('/cart')
def cart():
    return render_template("cart.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/checkout')
def checkout():
    return render_template("checkout.html")

@app.route('/store')
def store():
    return render_template("store.html")

@app.route('/testSTORE')
def test():
    return render_template("testSTORE.html")

@app.route('/index2')
def index2():
    return render_template("index2.html")


@app.route('/jeopardy')
def jeopardy():
    return render_template("jeopardy.html")
@app.route('/scratch')
def scratch():
    return render_template("pabl/scratch.html")
# @app.route('/basketball/', methods=['GET', 'POST'])
# def basketball():
#   url = "http://localhost:5000/api/basketball_api"
#   response = requests.request("GET", url)
#   return render_template("ritvik.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)