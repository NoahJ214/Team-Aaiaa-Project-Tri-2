# import "packages" from flask
import json


from api.web_api import app_api
from api.nfl import nfl_nfl
from api.tennis import app_tennis
from api.soccer import app_soccer
from api.baseball import app_baseball
from crud.app_crud import app_crud
from flask import render_template, request, Flask

# create a Flask instance
app = Flask(__name__)
app.register_blueprint(app_api)
app.register_blueprint(nfl_nfl)
app.register_blueprint(app_tennis)
app.register_blueprint(app_soccer)
app.register_blueprint(app_baseball)
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

# @app.route('/basketball/', methods=['GET', 'POST'])
# def basketball():
 #   url = "http://localhost:5000/api/basketball_api"
 #   response = requests.request("GET", url)
 #   return render_template("ritvik.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
