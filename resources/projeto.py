from flask_restful import Resource

from models.projeto import ProjetoModel


class Projetos(Resource):
    def get(self):        
        return {'projetos': [projeto.json() for projeto in ProjetoModel.list_projetos()]}, 200


class Projeto(Resource):
    def get(self, codigo_sequencial_projeto):
        projeto = ProjetoModel.find_projeto(codigo_sequencial_projeto)
        if projeto:
            return projeto.json()

        return {'message': 'Projeto not found.'}, 404
