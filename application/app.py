from flask import Flask
from flask_restful import Api
from .resources.marvel_randomizer import MarvelRandomizer


app = Flask(__name__)
api = Api(app)

api.add_resource(MarvelRandomizer, '/randomizer')


@app.route("/")
def index():
    """Index."""
    return "You have hit the index. That's cool."


@app.route("/randomizer/")
def marvel_randomizer():
    """Cool."""
    return MarvelRandomizer.get()
