from flask_restx import Namespace, Resource

namespace = Namespace('Migraciones', description='Recurso para migraciones a la base de datos')

@namespace.route('')
class PokemonMigration(Resource):
    
    def post(self):
        pass
