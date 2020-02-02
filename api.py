from flask import Flask
from flask import Flask, request
# from flask_restfull import Resource, Api
import flask_restful as restfull


app = Flask(__name__)
api = restfull.Api(app)

# define class name
class managerCity(restfull.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(managerCity, '/')

if __name__ == '__main__':
    app.run(debug=True)