from flask_restful import Resource

from models.tipo_unidade import TipoUnidadeModel


class TipoUnidades(Resource):
    def get(self):        
        return {'tipos_unidade': [tipo_unidade.json() for tipo_unidade in TipoUnidadeModel.list_tipo_unidades()]}, 200


class TipoUnidade(Resource):
    def get(self, codigo_tipo_unidade):
        tipo_unidade = TipoUnidadeModel.find_tipo_unidade(codigo_tipo_unidade)
        if tipo_unidade:
            return tipo_unidade.json()

        return {'message': 'Tipo Unidade not found.'}, 404
