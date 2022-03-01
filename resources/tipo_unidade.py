from flask_restful import Resource


tipo_unidades = [
    {
        'codigo_tipo_unidade': 80,
        'descricao_tipo_unidade': 'LABORATORIO DE SAUDE PUBLICA'
    },
    {
        'codigo_tipo_unidade': 81,
        'descricao_tipo_unidade': 'CENTRAL DE REGULACAO DO ACESSO'
    },
    {
        'codigo_tipo_unidade': 82,
        'descricao_tipo_unidade': 'OFICINA ORTOPEDICA'
    }
]


class TipoUnidades(Resource):
    def get(self):
        return {'tipos_unidade': tipo_unidades}, 200


class TipoUnidade(Resource):
    def find_tipo_unidade(codigo_tipo_unidade):
        for tipo_unidade in tipo_unidades:
            if tipo_unidade['codigo_tipo_unidade'] == codigo_tipo_unidade:
                return tipo_unidade
        return None

    def get(self, codigo_tipo_unidade):
        tipo_unidade = TipoUnidade.find_tipo_unidade(codigo_tipo_unidade)
        if tipo_unidade:
            return tipo_unidade

        return {'message': 'Tipo Unidade not found.'}, 404
