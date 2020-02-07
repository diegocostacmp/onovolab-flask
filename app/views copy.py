from flask import Blueprint, current_app, request, jsonify
from .model import City
from .serializer import CitySchema

bp_citys = Blueprint('citys', __name__)

@bp_citys.route('/', methods=['GET'])
def show():
    # i need consult webservice and 
    # keep json data in database
    
    

@bp_citys.route('/cidade/<id_da_cidade>', methods=['POST', 'GET'])
def register(id_da_cidade):
    # i need consult webservice and 
    # keep json data in database
    token_id = '15?token=b22460a8b91ac5f1d48f5b7029891b53'
    url_endpoint = 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/' + str(id_da_cidade) + '/days/' + token_id
    r = get(url_endpoint)
    data_json = r.json()
    


    schema = CitySchema()
    result = schema.load(request.json)

    # if error:
    #     return jsonify(error), 401

    current_app.db.session.add(result)
    current_app.db.session.commit()
    return schema.jsonify(result), 201


@bp_citys.route('/analyze', methods=['GET'])
def analyze():
    cs = CitySchema(many=True)
    result = City.query.all()
    return bs.jsonify(result), 200