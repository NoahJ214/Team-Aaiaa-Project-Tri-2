import random

from flask import Blueprint, jsonify

app_soccer = Blueprint('soccerapi', __name__,
                       url_prefix='/soccer_api',
                       template_folder='templates',
                       static_folder='static', static_url_path='static/soccer_api')

soccer_data = []
soccer_list = [
    "You have chosen Manchester City",
    "You have chosen Liverpool",
    "You have chosen Chelsea",
    "You have chosen West Ham",
    "You have chosen Tottenham",
    "You have chosen Manchester United",
    "You have chosen Arsenal",
    "You have chosen Wolves",
    "You have chosen Brighton",
    "You have chosen Aston Villa",
    "You have chosen Leicester City",
    "You have chosen Everton",
    "You have chosen Brentford",
    "You have chosen Crystal Palace",
    "You have chosen Leeds United",
    "You have chosen Southampton",
    "You have chosen Watford",
    "You have chosen Burnley",
    "You have chosen Newcastle",
    "You have chosen Norwich City"

]


def _init_soccer():
    item_id = 1
    for item in soccer_list:
        soccer_data.append({"id": item_id, "soccer": item})
        item_id += 1


@app_soccer.route('/soccer')
def soccer():
    if len(soccer_data) == 0:
        _init_soccer()
    return jsonify(random.choice(soccer_data))


if __name__ == "__main__":
    print(random.choice(soccer_list))