from flask_restful import Resource, reqparse

from models.estabelecimento import EstabelecimentoModel


DEFAULT_LIMIT = 5
MAX_LIMIT = 20


def normalize_path_params(codigo_tipo_unidade=None,
                            estabelecimento_possui_centro_cirurgico=None,
                            estabelecimento_possui_centro_obstetrico=None,
                            limit=DEFAULT_LIMIT,
                            offset=0,
                            **params):
    result_data = {}

    if codigo_tipo_unidade:
        result_data['codigo_tipo_unidade'] = codigo_tipo_unidade

    if estabelecimento_possui_centro_cirurgico is not None:
        result_data['estabelecimento_possui_centro_cirurgico'] = estabelecimento_possui_centro_cirurgico

    if estabelecimento_possui_centro_obstetrico is not None:
        result_data['estabelecimento_possui_centro_obstetrico'] = estabelecimento_possui_centro_obstetrico

    if limit > MAX_LIMIT:
        limit = MAX_LIMIT
    result_data['limit'] = limit

    result_data['offset'] = offset

    return result_data


class Estabelecimentos(Resource):
    def get(self):
        path_params = reqparse.RequestParser()
        path_params.add_argument('codigo_tipo_unidade', type=int)
        path_params.add_argument('estabelecimento_possui_centro_cirurgico', type=int)
        path_params.add_argument('estabelecimento_possui_centro_obstetrico', type=int)
        path_params.add_argument('limit', type=int)
        path_params.add_argument('offset', type=int)

        params_received = path_params.parse_args()
        params_received = {key:params_received[key] for key in params_received if params_received[key] is not None}        
        params_normalized = normalize_path_params(**params_received)

        return {'estabelecimentos': [estabelecimento.json() for estabelecimento in EstabelecimentoModel.list_estabelecimentos(**params_normalized)]}, 200


class Estabelecimento(Resource):
    def get(self, codigo_cnes):
        estabelecimento = EstabelecimentoModel.find_estabelecimento(codigo_cnes)
        if estabelecimento:
            return estabelecimento.json()

        return {'message': 'Estabelecimento not found.'}, 404
