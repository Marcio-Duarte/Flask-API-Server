from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Marcio",
        "age": 39,
        "nationality": "Portuguese"
    },
    {
        "name": "Bisrate",
        "age": "130",
        "Ocupation": "DCI"
    },
    {
        "name": "Younes",
        "age": 200,
        "occupation": "Student at DCI"
    }
]


class User(Resource):
    def get(self, name):
        for user in users:
            if name == user["name"]:
                return user, 200
        return "Name not found", 404


class AllUsers(Resource):
    def get(self):
        return users, 200


api.add_resource(User, "/name/<string:name>")
api.add_resource(AllUsers, "/all")

app.run(debug=True, host='0.0.0.0', port=8888)
