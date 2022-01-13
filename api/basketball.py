import random

from flask import Blueprint, jsonify, render_template

nba_api = Blueprint('api', __name__,
                    url_prefix='/nba_api',
                    template_folder='templates',
                    static_folder='static', static_url_path='static/nba_api')

nba_data = []
nba_list = [
    "You have chosen the Atlanta Hawks",
    "You have chosen the Boston Celtics",
    "You have chosen the Brooklyn Nets",
    "You have chosen the Charlotte Hornets",
    "You have chosen the Chicago Bulls",
    "You have chosen the Cleveland Cavaliers",
    "You have chosen the Dallas Mavericks",
    "You have chosen the Denver Nuggets",
    "You have chosen the Detroit Pistons",
    "You have chosen the Golden State Warriors",
    "You have chosen the Houston Rockets",
    "You have chosen the Indiana Pacers",
    "You have chosen the Los Angeles Clippers",
    "You have chosen the Los Angeles Lakers",
    "You have chosen the Memphis Grizzlies",
    "You have chosen the Miami Heat",
    "You have chosen the Milwaukee Bucks",
    "You have chosen the Minnesota Timberwolves",
    "You have chosen the New Orleans Pelicans",
    "You have chosen the New York Knicks",
    "You have chosen the Oklahoma City Thunder",
    "You have chosen the Orlando Magic",
    "You have chosen the Philadelphia 76ers",
    "You have chosen the Phoenix Suns",
    "You have chosen the Portland Trail Blazers",
    "You have chosen the Sacramento Kings",
    "You have chosen the San Antonio Spurs",
    "You have chosen the Toronto Raptors",
    "You have chosen the Utah Jazz",
    "You have chosen the Washington Wizards"
]

locations = [
    "Atlanta",
    "Boston",
    "Brooklyn",
    "Charlotte",
    "Chicago",
    "Cleveland",
    "Dallas",
    "Denver",
    "Detroit",
    "San Fransisco",
    "Houston",
    "Indiana",
    "Los Angeles",
    "Los Angeles",
    "Memphis",
    "Miami",
    "Milwaukee",
    "Minnesota",
    "New Orleans",
    "New York",
    "Oklahoma",
    "Orlando",
    "Philadelphia",
    "Phoenix",
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


