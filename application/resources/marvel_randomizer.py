from flask import request
from flask_restful import Resource


def generate_game(request_data):
    """Return a valid game of Marvel Legendary."""
    return {"game": "gamessss"}


class MarvelRandomizer(Resource):
    """The Marvel Randomizer."""

    def post(self):
        """Genereate a new game."""
        print(request.form['data'])
        return generate_game(request.form['data'])
