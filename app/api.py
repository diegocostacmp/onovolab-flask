from flask import Blueprint, current_app, request, jsonify
from .model import City
from .serializer import CitySchema
from requests import get, post
import json
from datetime import date, datetime
from sqlalchemy import desc, func
from unidecode import unidecode


bp_citys = Blueprint('citys', __name__)    

@bp_citys.route('/cidade/<id_da_cidade>/', methods=['GET'])
def register(id_da_cidade):
    # i need consult webservice and 
    # keep json data in database
    token_id = '15?token=b22460a8b91ac5f1d48f5b7029891b53'
    url_endpoint = 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/' + str(id_da_cidade) + '/days/' + token_id
    r = get(url_endpoint)
    data_json = r.json()

    for i in data_json['data']:
        
        dt = i["date_br"].split('/')
        day_ = int(dt[0])
        month_ = int(dt[1])
        year_ = int(dt[2])
        date_br = date(day=day_, 
            month=month_,
            year=year_).strftime('%d/%m/%Y')

        dados = {
            "name":data_json["name"],
            "state": str(data_json["state"]),
            "country": data_json["country"],
            "date": str(date_br),
            "precipitation": str(i["rain"]["precipitation"]),
            'probability': str(i["rain"]["probability"]),
            "max_": str(i["temperature"]["max"]),
            "min_": str(i["temperature"]["min"])
        }
        
        schema = CitySchema()
        data_item = str(dados).replace("\'", "\"")
        result = schema.load(json.loads(data_item))

        current_app.db.session.add(result)
        current_app.db.session.commit()

    return schema.jsonify(data_json), 201


@bp_citys.route('/analise/<start>/<end>/', methods=['GET'])
def analise(start, end):
    start = str(start).split('-')
    start_day = int(start[0])
    start_month = int(start[1])
    start_year = int(start[2])

    end = str(end).split('-')
    end_day = int(end[0])
    end_month = int(end[1])
    end_year = int(end[2])

    # example: start = 07/02/2020, end = 12/02/202
    start = date(day=start_day, 
        month=start_month, 
        year=2020).strftime('%d/%m/%Y')

    end = date(day=end_day, 
        month=end_month, 
        year=end_year).strftime('%d/%m/%Y')

    data = City.query.filter(City.date <= end).filter(City.date >= start)
    data = data.order_by(desc(City.name))
    data2 = data.order_by(desc(City.name))
    
    # methods
    temperature = max_temperature(data)
    precipitation = avg_precipitation(data)

    return jsonify(temperature + precipitation)

def max_temperature(data):
    try:
        bigger = 0
        count = 0
        list_max = []
        res_list = [] 
        
        # get max temperature from data set
        for i in data:
            if int(i.max_) > bigger:
                bigger = int(i.max_)
                count = count + 1
            else:
                count = count + 1
            if count == data.count():
                name_city = str(i.name)
                max_temp = int(bigger)

        # Checked if there are other cities with 
        # temperatures equal to the highest obtained
        for j in data:
            if int(j.max_) == max_temp:
                list_max.append({
                    unidecode(str(j.name)): int(j.max_)
                })

        # Removing the repeated, since more than one
        # city can have equal maximum temperatures
        for i in range(len(list_max)): 
            if list_max[i] not in list_max[i + 1:]: 
                res_list.append({
                    "maior temperatura": list_max[i]
                    }) 
    except:
        res_list = {
            'excecao': 'Delculpe tivemos alguma problema ao aexecutar o metodo max_temperature'
        }
    return res_list
                

def avg_precipitation(data):
    try:
        city = ''
        sum_total = 0
        count = 0
        count2 = 0
        list_precipitation = []

        for i in data:
            if city == '':
                city = i.name
                sum_total = sum_total + int(i.precipitation)
                count = count + 1
                count2 = count2 + 1
            elif city == i.name:
                # still equal city
                sum_total = sum_total + int(i.precipitation)
                count = count + 1
                count2 = count2 + 1
                if data.count() == count2:
                    list_precipitation.append({
                    "cidade com maior precipitacao": str(city) + ' - ' + str((sum_total / count))
                })
            else:
                list_precipitation.append({
                    "cidade com maior precipitacao": str(city) + ' - ' + str((sum_total / count))
                })

                # clearing info by old city
                city = i.name
                count = 0
                sum_total = 0

                # global informations about sum_total
                sum_total = sum_total + int(i.precipitation)
                count = count + 1
                count2 = count2 + 1
    except :
        list_precipitation = {
            'excecao': 'Delculpe, tivemos algum problema ao executar o metodo avg_precipitation' 
        }
    return list_precipitation