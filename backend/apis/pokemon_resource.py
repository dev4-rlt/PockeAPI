from flask_restx import Namespace, Resource, fields

api = Namespace('pokemones', description='Recurso para pokemones')

@api.route('/')
class PokemonesResource(Resource):

    def get(self):
        return []