from flask_restx import Namespace, Resource, fields, reqparse, abort
from core.database import db, Habilities
from apis.models import abilityModel, pokemonAbilityModel

namespace = Namespace('Ability', description='Recurso para habilidades')

abilityDetails = namespace.inherit('AbilityDetails', abilityModel, {
    'pokemonsAbility': fields.List(fields.Nested(pokemonAbilityModel))
})

postAbility = namespace.model(name='PostAbility', model={
    'name': fields.String,
    'description': fields.String,
})

@namespace.route('')
class HabilitiesResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)

    @namespace.expect(parser)
    @namespace.marshal_with(abilityDetails, as_list=True)
    def get(self):
        args = self.parser.parse_args()
        
        query = db.session.query(Habilities)

        if 'name' in args and args['name'] != None:
            query = query.filter(Habilities.name.like('%'+args['name']+'%'))

        return query.all()
    
    @namespace.expect(postAbility, validate=True)
    @namespace.marshal_with(abilityDetails)
    def post(self):
        body = namespace.payload

        newAbility = Habilities()
        newAbility.name = body['name']
        
        if 'description' in body:
            newAbility.description = body['description']

        db.session.add(newAbility)
        db.session.commit()

        return newAbility

@namespace.route('/<int:codAbility>')
class AbilitiesResource(Resource):

    @namespace.marshal_with(abilityDetails)
    def get(self, codAbility: int):
        ability: Habilities = db.session.query(Habilities).get(codAbility)
        if ability is None:
            abort(404, 'No se encuentra la habilidad buscada')
        return ability
    
    @namespace.expect(postAbility, validate=True)
    @namespace.marshal_with(abilityDetails)
    def put(self, codAbility: int):
        body = namespace.payload

        ability: Habilities = db.session.query(Habilities).get(codAbility)
        if ability == None:
            abort(404, 'No se encuentra la habilidad')

        try:
            ability.name = body['name']
            ability.name = body['description']
            db.session.commit()
        except:
            abort(500)
            
        return ability