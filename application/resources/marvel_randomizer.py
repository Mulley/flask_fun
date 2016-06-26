import random
from flask_restful import abort, reqparse, Resource
from application.common import cards


parser = reqparse.RequestParser()
parser.add_argument('players', type=int, required=True,
                    help="You didn't specify the amount of players!")
parser.add_argument('expansion', type=str, action='append')


def generate_game(request_data):
    """Return a valid game of Marvel Legendary."""
    data_to_return = {'Heroes': [], 'Scheme': ''}
    data_to_pick = {'Heroes': [], 'Schemes': []}

    # Generate List of Heroes From Which to Pick
    for expansion in request_data['expansion']:
        data_to_pick['Heroes'].extend(cards.HEROES[expansion])
        data_to_pick['Schemes'].extend(cards.SCHEMES[expansion])

    # Return Heroes
    if request_data['players'] != 5:
        data_to_return['Heroes'].extend(
            random.sample(data_to_pick['Heroes'], 5))
    else:
        data_to_return['Heroes'].extend(
            random.sample(data_to_pick['Heroes'], 6))

    for i, hero in enumerate(data_to_return['Heroes']):
        data_to_return['Heroes'][i] = hero['Name']

    # Pick a Scheme
    data_to_return['Scheme'] = random.choice(data_to_pick['Schemes'])
    return data_to_return


class MarvelRandomizer(Resource):
    """The Marvel Randomizer."""

    def post(self):
        """Genereate a new game."""
        request_data = parser.parse_args()
        # Check Parsed Data
        if request_data['players'] not in cards.PLAYER_AMOUNT:
            abort(400, message="Invalid amount of players specified.")
        if request_data['expansion']:
            for expansion in request_data['expansion']:
                if expansion not in cards.Expansions.__members__:
                    abort(400,
                          message="Invalid expansion '{}''".format(expansion))
        else:
            # Use all expansions
            request_data['expansion'] = list(
                map(str, cards.Expansions.__members__))
        return generate_game(request_data)
