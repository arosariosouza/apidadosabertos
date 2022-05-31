from flask_restful import Resource, reqparse

from models.projeto import ProjetoModel


DEFAULT_LIMIT = 5
MAX_LIMIT = 20


def normalize_path_params(uf_comite_etica_pesquisa=None,
                            codigo_situacao_parecer=None,
                            uf_instituicao_proponente=None,
                            limit=DEFAULT_LIMIT,
                            offset=0,
                            **params):
    result_data = {}

    if uf_comite_etica_pesquisa:
        result_data['uf_comite_etica_pesquisa'] = uf_comite_etica_pesquisa

    if codigo_situacao_parecer is not None:
        result_data['codigo_situacao_parecer'] = codigo_situacao_parecer

    if uf_instituicao_proponente is not None:
        result_data['uf_instituicao_proponente'] = uf_instituicao_proponente

    if limit > MAX_LIMIT:
        limit = MAX_LIMIT
    result_data['limit'] = limit

    result_data['offset'] = offset

    return result_data
    

class Projetos(Resource):
    def get(self):
        path_params = reqparse.RequestParser()
        path_params.add_argument('uf_comite_etica_pesquisa', type=str)
        path_params.add_argument('codigo_situacao_parecer', type=int)
        path_params.add_argument('uf_instituicao_proponente', type=str)
        path_params.add_argument('limit', type=int)
        path_params.add_argument('offset', type=int)

        params_received = path_params.parse_args()
        params_received = {key:params_received[key] for key in params_received if params_received[key] is not None}
        params_normalized = normalize_path_params(**params_received)

        return {'projetos': [projeto.json() for projeto in ProjetoModel.list_projetos(**params_normalized)]}, 200


class Projeto(Resource):
    def get(self, numero_caae):
        projeto = ProjetoModel.find_projeto(numero_caae.replace('.', ''))
        if projeto:
            return projeto.json()

        return {'message': 'Projeto not found.'}, 404
