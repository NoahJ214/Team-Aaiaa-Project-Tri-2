import random

from flask import Blueprint, jsonify
app_baseball = Blueprint('baseballapi', __name__,
                    url_prefix='/baseball_api',
                    template_folder='templates',
                    static_folder='static', static_url_path='static/baseball_api')

baseball_data = []
baseball_list = [
    "You have chosen the Atlanta Braves",
    "You have chosen the Miami Marlins",
    "You have chosen the New York Mets",
    "You have chosen the Philadelphia Phillies",
    "You have chosen the Washington Nationals",
    "You have chosen the Chicago Cubs",
    "You have chosen the Cincinnati Reds",
    "You have chosen the Milwaukee Brewers",
    "You have chosen the Pittsburgh Pirates",
    "You have chosen the St. Louis Cardinals",
    "You have chosen the Arizona Diamondbacks",
    "You have chosen the Colorado Rockies",
    "You have chosen the Los Angeles Dodgers",
    "You have chosen the San Diego Padres",
    "You have chosen the San Francisco Giants",
    "You have chosen the Baltimore Orioles",
    "You have chosen the Boston Red Sox",
    "You have chosen the New York Yankees",
    "You have chosen the Tampa Bay Rays",
    "You have chosen the Toronto Blue Jays",
    "You have chosen the Chicago White Sox",
    "You have chosen the Cleveland Indians",
    "You have chosen the Detroit Tigers",
    "You have chosen the Kansas City Royals",
    "You have chosen the Minnesota Twins",
    "You have chosen the Houston Astros",
    "You have chosen the Los Angeles Angels",
    "You have chosen the Oakland Athletics",
    "You have chosen the Seattle Mariners",
    "You have chosen the Texas Rangers",

]


def _init_baseball():
    item_id = 1
    for item in baseball_list:
        baseball_data.append({"id": item_id, "baseball": item})
        item_id += 1


@app_baseball.route('/baseball')
def baseball():
    if len(baseball_data) == 0:
        _init_baseball()
    return jsonify(random.choice(baseball_data))


if __name__ == "__main__":
    print(random.choice(baseball_list))