import random

from PIL import Image
from flask import Blueprint, jsonify, render_template

nba_api = Blueprint('api', __name__,
                    url_prefix='/nba_api',
                    template_folder='templates',
                    static_folder='static', static_url_path='static/nba_api')

nba_data = []


nba_list = [
    "You have chosen the Hawks",
    "You have chosen the Celtics",
    "You have chosen the Nets",
    "You have chosen the Hornets",
    "You have chosen the Bulls",
    "You have chosen the Cavaliers",
    "You have chosen the Mavericks",
    "You have chosen the Nuggets",
    "You have chosen the Pistons",
    "You have chosen the Golden State Warriors",
    "You have chosen the Rockets",
    "You have chosen the Pacers",
    "You have chosen the Clippers",
    "You have chosen the Lakers",
    "You have chosen the Grizzlies",
    "You have chosen the Heat",
    "You have chosen the Milwaukee Bucks",
    "You have chosen the Timberwolves",
    "You have chosen the Pelicans",
    "You have chosen the Knicks",
    "You have chosen the Thunder",
    "You have chosen the Magic",
    "You have chosen the 76ers",
    "You have chosen the Phoenix Suns",
    "You have chosen the Trail Blazers",
    "You have chosen the Kings",
    "You have chosen the Spurs",
    "You have chosen the Raptors",
    "You have chosen the Jazz",
    "You have chosen the Wizards"
]

locations = [
    "Atlanta",
    "Boston",
    "Brooklyn",
    "Charlotte",
    "Chicago",
    "Cleveland",
    "Dallas Texas",
    "Denver",
    "Detroit",
    "San Fransisco California",
    "Houston",
    "Indiana",
    "Los Angeles California",
    "Los Angeles California",
    "Memphis",
    "Miami",
    "Milwaukee",
    "Minnesota",
    "New Orleans",
    "New York",
    "Oklahoma",
    "Orlando",
    "Philadelphia",
    "Phoenix Arizona",
    "Portland ",
    "Sacramento",
    "San Antonio",
    "Toronto",
    "Utah",
    "Washington"
]


colors=[
    "#E03A3E",
    "#007A33",
    "#000000",
    "#1D1160",
    "#CE1141",
    "#860038",
    "#4169e1",
    "#191970",
    "#FF0000",
    "#006BB8",
    "#FF0000",
    "#002D62",
    "#FF0000",
    "#552583",
    "#0000FF",
    "#0000FF",
    "#00471B",
    "#191970",
    "#0C2340",
    "#006BB6",
    "#007AC1",
    "#0077C0",
    "#0000FF",
    "#7F00FF",
    "#FF0000",
    "#7F00FF",
    "#C0C0C0",
    "#FF0000",
    "#000080",
    "#000080"
]


def _init_nba():
    item_id = 1
    for item in nba_list:
        nba_data.append({"id": item_id, "nba": item, "location": locations[item_id-1]})
        item_id += 1


@nba_api.route('/nba')
def nba():
    if len(nba_data) == 0:
        _init_nba()
    id = random.randint(0, len(nba_data)-1)
    nba=nba_data[id]["nba"]
    location=locations[id]
    color=colors[id]
    return render_template("layouts/NBATEAMS.html", nba=nba, location=location, color=color)


if __name__ == "__main__":
    print(random.choice(nba_list))