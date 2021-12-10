import random

from flask import Blueprint, jsonify
nfl_nfl = Blueprint('notapi', __name__,
                   url_prefix='/football_api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/football_api')

nfl_data = []
nfl_list = [
    "You have chosen the Arizona Cardinals",
    "You have chosen the Atlanta Falcons",
    "You have chosen the Baltimore Ravens",
    "You have chosen the Buffalo Bills",
    "You have chosen the Carolina Panthers",
    "You have chosen the Chicago Bears",
    "You have chosen the Cincinnati Bengals",
    "You have chosen the Cleveland Browns",
    "You have chosen the Dallas Cowboys",
    "You have chosen the Denver Broncos",
    "You have chosen the Detroit Lions",
    "You have chosen the Green Bay Packers",
    "You have chosen the Houston Texans",
    "You have chosen the Indianapolis Colts",
    "You have chosen the Jacksonville Jaguars",
    "You have chosen the Kansas City Chiefs",
    "You have chosen the Las Vegas Raiders",
    "You have chosen the Las Vegas Raiders",
    "You have chosen the San Diego Chargers",
    "You have chosen the Los Angeles Rams",
    "You have chosen the Miami Dolphins",
    "You have chosen the Minnesota Vikings",
    "You have chosen the New England Patriots",
    "You have chosen the New Orleans Saints",
    "You have chosen the New York Giants",
    "You have chosen the New York Jets",
    "You have chosen the Philadelphia Eagles",
    "You have chosen the Pittsburgh Steelers",
    "You have chosen the San Francisco 49ers",
    "You have chosen the Seattle Seahawks",
    "You have chosen the Tampa Bay Buccaneers",
    "You have chosen the Tennessee Titans",
    "You have chosen the Washington Football Team"


]


def _init_nfl():
    item_id = 1
    for item in nfl_list:
        nfl_data.append({"id": item_id, "nfl": item})
        item_id += 1


@nfl_nfl.route('/nfl')
def nfl():
    if len(nfl_data) == 0:
        _init_nfl()
    return jsonify(random.choice(nfl_data))


if __name__ == "__main__":
    print(random.choice(nfl_list))