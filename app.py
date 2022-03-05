#!/usr/bin/env python
import urllib.parse

from flask import Flask, render_template
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

from decouple import config

from sql_alchemy import database
from resources.estabelecimento import Estabelecimentos, Estabelecimento
from resources.tipo_unidade import TipoUnidades, TipoUnidade


DEBUG = config('DEBUG', default=False, cast=bool)
HOST = config('HOST', default='127.0.0.1')

SQLALCHEMY_DATABASE_USER = config('SQLALCHEMY_DATABASE_USER', default= '')
SQLALCHEMY_DATABASE_PASSWORD = urllib.parse.quote_plus(config('SQLALCHEMY_DATABASE_PASSWORD', default= ''))
SQLALCHEMY_DATABASE_SERVER = config('SQLALCHEMY_DATABASE_SERVER', default= '')
SQLALCHEMY_DATABASE_DATABASE = config('SQLALCHEMY_DATABASE_DATABASE', default= '')
SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s/%s' \
    % (SQLALCHEMY_DATABASE_USER, SQLALCHEMY_DATABASE_PASSWORD, SQLALCHEMY_DATABASE_SERVER, SQLALCHEMY_DATABASE_DATABASE)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config('SQLALCHEMY_TRACK_MODIFICATIONS', default=False, cast=bool)

SWAGGER_URL = '/api'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config = {
        'app_name': 'DEMAS - API de Dados Abertos'
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

database.init_app(app)

api = Api(app)

api.add_resource(Estabelecimentos, '/estabelecimentos')
api.add_resource(Estabelecimento, '/estabelecimentos/<int:codigo_cnes>')
api.add_resource(TipoUnidades, '/tipounidades')
api.add_resource(TipoUnidade, '/tipounidades/<int:codigo_tipo_unidade>')


@app.route('/')
def home():
    return render_template('home.html') 


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST)
