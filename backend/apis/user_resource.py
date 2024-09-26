from flask_restx import Namespace, fields, Resource, reqparse
from core.database import db, Users
from apis.models import userModel

namespace = Namespace('User', description='Recurso para manejo de usuarios')

postUser = namespace.model(name='PostUser', model={
    'name': fields.String,
    'username': fields.String,
    'password': fields.String,
    'address': fields.String
})

@namespace.route('/login')
class UsersResource(Resource):

    @namespace.expect(postUser, validate=True)
    @namespace.marshal_with(userModel)
    def post(self):
        body = namespace.payload
        
        query = db.session.query(Users).filter(Users.username == body['username']).filter(Users.password == body['password'])
        response = query.all()
        
        if len(response) > 0:
            return response[0], 200
        else:
            return { 'message': 'Credenciales incorrectas' }, 401