import random

from flask import Blueprint, jsonify

app_tennis = Blueprint('tennisapi', __name__,
                    url_prefix='/tennis_api',
                    template_folder='templates',
                    static_folder='static', static_url_path='static/tennis_api')

tennis_data = []
tennis_list = [
    "You have chosen Novak Djokovic",
    "You have chosen Danill Medvedev",
    "You have chosen Alexander Zverev",
    "You have chosen Stefanos Tsitspas",
    "You have chosen Andrey Reblev",
    "You have chosen Rafael Nadal",
    "You have chosen Matteo Berrenttini",
    "You have chosen Casper Ruud",
    "You have chosen Hubert Hurkacz",
    "You have chosen Jannik Sinner",
    "You have chosen Felix Auger-Aliassime",
    "You have chosen Cameron Norrie",
    "You have chosen Diego Schwartzman",
    "You have chosen Denis Shapovalov",
    "You have chosen Dominic Thiem",
    "You have chosen Roger Federer",
    "You have chosen Cristian Garin",
    "You have chosen Aslan Karatsev",
    "You have chosen Roberto Bautista Agut",
    "You have chosen Pablo Carreno Busta",
    "You have chosen Gael Monfilis",
    "You have chosen Nikoloz Basilashvili",
    "You have chosen Taylor Fritz",
    "You have chosen John Isner",
    "You have chosen Daniel Evans",
    "You have chosen Reily Opelka"
]


def _init_tennis():
    item_id = 1
    for item in tennis_list:
        tennis_data.append({"id": item_id, "tennis": item})
        item_id += 1


@app_tennis.route('/tennis')
def tennis():
    if len(tennis_data) == 0:
        _init_tennis()
    return jsonify(random.choice(tennis_data))


if __name__ == "__main__":
    print(random.choice(tennis_list))