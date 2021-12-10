import random

from flask import Blueprint, jsonify
nfl_api = Blueprint('api', __name__,
                   url_prefix='/football_api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/football_api')

nfl_data = []
nfl_list = [
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


def _init_nfl():
    item_id = 1
    for item in nfl_list:
        nfl_data.append({"id": item_id, "nfl": item})
        item_id += 1


@nfl_api.route('/nfl')
def nfl():
    if len(nfl_data) == 0:
        _init_nfl()
    return jsonify(random.choice(nfl_data))


if __name__ == "__main__":
    print(random.choice(nfl_list))