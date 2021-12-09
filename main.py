# import "packages" from flask
import requests
import json
from flask import render_template, request, Flask

# create a Flask instance
app = Flask(__name__)

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

    url = "https://sportscore1.p.rapidapi.com/teams"

    querystring = {"page":"1"}

    headers = {
        'x-rapidapi-host': "sportscore1.p.rapidapi.com",
        'x-rapidapi-key': "bc9e5f20f9mshfceb3f679afd2b7p1960cdjsn87cb096651ab"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # return(response.json())
    data = json.loads(response.text)
    return render_template("ritvik.html", output=response.json())



@app.route('/nathan/')
def Nathan():
    return render_template("nathan.html")

@app.route('/william/')
def William():
    return render_template("william.html")

@app.route('/noah/')
def Noah():
    return render_template("noah.html")

@app.route('/basketball/', methods=['GET', 'POST'])
def basketball():
    url = "http://localhost:5000/api/basketball_api"
    response = requests.request("GET", url)
    return render_template("ritvik.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
