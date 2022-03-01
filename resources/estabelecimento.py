from flask_restful import Resource


estabelecimentos = [
    {
        'codigo_cnes': 27,
        'numero_cnpj_entidade': '10930451000181',
        'nome_razao_social': 'CASA DE SAUDE E MATERNIDADE SANTA HELENA LTDA',
        'nome_fantasia': 'CASA DE SAUDE SANTA HELENA',
        'natureza_organizacao_entidade': None,
        'tipo_gestao': 'M',
        'descricao_nivel_hierarquia': None,
        'descricao_esfera_administrativa': None,
        'codigo_tipo_unidade': 5,
        'codigo_cep_estabelecimento': '54505560',
        'endereco_estabelecimento': 'AVN PRESIDENTE GETULIO VARGAS',
        'numero_estabelecimento': '428',
        'bairro_estabelecimento': 'CENTRO',
        'numero_telefone_estabelecimento': '(81)35210355',
        'latitude_estabelecimento_decimo_grau': -8.287,
        'longitude_estabelecimento_decimo_grau': -35.035,
        'endereco_email_estabelecimento': None,
        'numero_cnpj': '10930451001153',
        'codigo_identificador_turno_atendimento': '06',
        'descricao_turno_atendimento': 'ATENDIMENTO CONTINUO DE 24 HORAS/DIA (PLANTAO:INCLUI SABADOS, DOMINGOS E FERIADOS)',
        'estabelecimento_faz_atendimento_ambulatorial_sus': 'SIM',
        'codigo_estabelecimento_saude': '2602900000027',
        'codigo_uf': 26,
        'codigo_ibge_municipio': 260290,
        'descricao_natureza_juridica_estabelecimento': '2062',
        'codigo_motivo_desabilitacao_estabelecimento': None,
        'estabelecimento_possui_centro_cirurgico': 1,
        'estabelecimento_possui_centro_obstetrico': 1,
        'estabelecimento_possui_centro_neonatal': 1,
        'estabelecimento_possui_atendimento_hospitalar': 1,
        'estabelecimento_possui_servico_apoio': 1,
        'estabelecimento_possui_atendimento_ambulatorial': 1,
        'codigo_atividade_ensino_unidade': '04',
        'codigo_natureza_organizacao_unidade': None,
        'codigo_nivel_hierarquia_unidade': None,
        'codigo_esfera_administrativa_unidade': None
    }
]


class Estabelecimentos(Resource):
    def get(self):
        return {'estabelecimentos': estabelecimentos}, 200

class Estabelecimento(Resource):
    def find_estabelecimento(codigo_cnes):
        for estabelecimento in estabelecimentos:
            if estabelecimento['codigo_cnes'] == codigo_cnes:
                return estabelecimento
        return None
    
    def get(self, codigo_cnes):
        estabelecimento = Estabelecimento.find_estabelecimento(codigo_cnes)
        if estabelecimento:
            return estabelecimento

        return {'message': 'Estabelecimento not found.'}, 404
