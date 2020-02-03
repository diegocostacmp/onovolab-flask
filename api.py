from flask import Flask, json
from flask import Flask, request
import flask_restful as restfull
from  requests import get



app = Flask(__name__)
api = restfull.Api(app)


# define class name
class managerCity(restfull.Resource):
    def get(self, id_city):
        # url defined to onovoLab
        encoding = 'utf-8'
        headers = 'application/json; charset=utf8'
        url_endpoint = 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/' + str(id_city) + '/days/15?token=b22460a8b91ac5f1d48f5b7029891b53'
        r = get(url_endpoint)
        data_json = r.json()
        return data_json

api.add_resource(managerCity, '/city/<int:id_city>')

if __name__ == '__main__':
    app.run(debug=True)