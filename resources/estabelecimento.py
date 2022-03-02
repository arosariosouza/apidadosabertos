from flask_restful import Resource

from models.estabelecimento import EstabelecimentoModel


class Estabelecimentos(Resource):
    def get(self):
        return {'estabelecimentos': [estabelecimento.json() for estabelecimento in EstabelecimentoModel.list_estabelecimentos()]}, 200


class Estabelecimento(Resource):
    def get(self, codigo_cnes):
        estabelecimento = EstabelecimentoModel.find_estabelecimento(codigo_cnes)
        if estabelecimento:
            return estabelecimento.json()

        return {'message': 'Estabelecimento not found.'}, 404
