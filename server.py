from flask import Flask
from flask_restful import Api, Resource, reqparse
import data as users; 

app = Flask(__name__)
api = Api(app)
users = users.users_list

# -- Routes -- #
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

# -- Run and debug the Flask server -- #
app.run(debug=True, host='0.0.0.0', port=8888)