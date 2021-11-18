# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html

@app.route('/william/')
def greet6():
    return render_template("william.html")

@app.route('/william/', methods=['GET', 'POST'])
def greet7():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("william.html", name1=name)
    # starting and empty input default
    return render_template("william.html", name1="World")







@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route("/ritvik/")
def ritvik():
    return render_template("ritvik.html")

@app.route("/william/")
def william():
    return render_template("william.html")

@app.route("/timothy/")
def timothy():
    return render_template("timothy.html")

@app.route("/nathan/")
def nathan():
    return render_template("nathan.html")

@app.route("/noah")
def noah():
    return render_template("noah.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)