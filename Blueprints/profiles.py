from flask import Blueprint, render_template, request
import requests
import json

profiles = Blueprint('profiles', __name__,
                     url_prefix='/',
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')


@profiles.route('/timmy/')
def Timmy():
    return render_template("timothy.html")


@profiles.route('/ritvik/', methods=['GET', 'POST'])
def Ritvik():
    return render_template("ritvik.html")



@profiles.route('/nathan/')
def Nathan():
    return render_template("nathan.html")

@profiles.route('/william/')
def William():
    return render_template("william.html")

@profiles.route('/noah/')
def Noah():
    return render_template("noah.html")