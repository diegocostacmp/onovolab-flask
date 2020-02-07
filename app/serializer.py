from marshmallow import fields, validates, ValidationError, Schema
from flask_marshmallow import Marshmallow
from .model import City 

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class CitySchema(ma.ModelSchema):
    class Meta:
        model = City