from flask_restx import fields
from apis import api

locationModel = api.model(name='LocationModel', model={
    'codLocation': fields.Integer,
    'name': fields.String,
})

abilityModel = api.model(name='AbilityModel', model={
    'codHability': fields.Integer,
    'name': fields.String,
    'description': fields.String
})

gameModel = api.model(name='GameModel', model={
    'codGame': fields.Integer,
    'name': fields.String,
})

moveModel = api.model(name='MoveModel', model={
    'codMove': fields.Integer,
    'name': fields.String,
    'description': fields.String,
})

pokemonModel = api.model(name='PokemonModel', model={
    'codPokemon': fields.Integer,
    'name': fields.String,
    'height': fields.Integer,
    'weight': fields.Integer,
    'hp': fields.Integer,
    'attack': fields.Integer,
    'defense': fields.Integer,
    'specialAttack': fields.Integer,
    'specialDefense': fields.Integer,
    'speed': fields.Integer,
    'spriteFrontDefault': fields.String,
    'spriteFrontShiny': fields.String
})

# Tablas intermedias

pokemonGameModel = api.model(name='PokemonGameModel', model={
    'codPokemonGame': fields.Integer,
    'pokemonCod': fields.Integer,
    'pokemonName': fields.String(attribute='pokemon.name'),
    'gameCod': fields.Integer,
    'gameName': fields.String(attribute='game.name')
})

pokemonAbilityModel = api.model(name='PokemonAbilityModel', model={
    'codPokemonAbility': fields.Integer,
    'pokemonCod': fields.Integer,
    'pokemonName': fields.String(attribute='pokemon.name'),
    'abilityCod': fields.Integer,
    'abilityName': fields.String(attribute='ability.name'),
    'abilityDescription': fields.String(attribute='ability.description')
})

pokemonMoveModel = api.model(name='PokemonMoveModel', model={
    'codPokemonMove': fields.Integer,
    'pokemonCod': fields.Integer,
    'pokemonName': fields.String(attribute='pokemon.name'),
    'moveCod': fields.Integer,
    'moveName': fields.String(attribute='move.name'),
    'moveDescription': fields.String(attribute='move.description')
})

pokemonLocationModel = api.model(name='PokemonLocationModel', model={
    'codPokemonLocation': fields.Integer,
    'pokemonCod': fields.Integer,
    'pokemonName': fields.String(attribute='pokemon.name'),
    'locationCod': fields.Integer,
    'locationName': fields.String(attribute='location.name')
})

# pokemonGameModel = api.model(name='PokemonGameModel', model={
#     'codPokemonGame': fields.Integer,
#     'pokemonCod': fields.Integer,
#     'gameCod': fields.Integer,
# })

# pokemonAbilityModel = api.model(name='PokemonAbilityModel', model={
#     'codPokemonAbility': fields.Integer,
#     'pokemonCod': fields.Integer,
#     'abilityCod': fields.Integer,
# })

# pokemonMoveModel = api.model(name='PokemonMoveModel', model={
#     'codPokemonMove': fields.Integer,
#     'pokemonCod': fields.Integer,
#     'moveCod': fields.Integer,
# })

# pokemonLocationModel = api.model(name='PokemonLocationModel', model={
#     'codPokemonLocation': fields.Integer,
#     'pokemonCod': fields.Integer,
#     'locationCod': fields.Integer,
# })

