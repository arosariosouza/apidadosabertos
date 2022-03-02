from sql_alchemy import database


class EstabelecimentoModel(database.Model):
    __tablename__ = 'tb_cnes_estabelecimento'
    __table_args__ = {'schema': 'dbacoes_saude'}

    codigo_cnes = database.Column('co_cnes', database.BigInteger, primary_key=True)
    numero_cnpj_entidade = database.Column('nu_cnpj_mantenedora', database.String(255))
    nome_razao_social = database.Column('no_razao_social', database.String(255))
    nome_fantasia = database.Column('no_fantasia', database.String(255))
    natureza_organizacao_entidade = database.Column('ds_natureza_organizacao', database.String(255))
    tipo_gestao = database.Column('tp_gestao', database.String(255))
    descricao_nivel_hierarquia = database.Column('ds_nivel_hierarquia', database.String(255))
    descricao_esfera_administrativa = database.Column('ds_esfera_administrativa', database.String(50))
    codigo_tipo_unidade = database.Column('tp_unidade', database.Integer)
    codigo_cep_estabelecimento = database.Column('co_cep', database.String(8))
    endereco_estabelecimento = database.Column('no_logradouro', database.String(150))
    numero_estabelecimento = database.Column('nu_endereco', database.String(10))
    bairro_estabelecimento = database.Column('no_bairro', database.String(80))
    numero_telefone_estabelecimento = database.Column('nu_telefone', database.String(60))
    latitude_estabelecimento_decimo_grau = database.Column('nu_latitude', database.Float(precision=3))
    longitude_estabelecimento_decimo_grau = database.Column('nu_longitude', database.Float(precision=3))
    endereco_email_estabelecimento = database.Column('no_email', database.String(60))
    numero_cnpj = database.Column('nu_cnpj', database.String(30))
    codigo_identificador_turno_atendimento = database.Column('co_turno_atendimento', database.String(2))
    descricao_turno_atendimento = database.Column('ds_turno_atendimento', database.String(100))
    estabelecimento_faz_atendimento_ambulatorial_sus = database.Column('co_ambulatorial_sus', database.String(3))
    codigo_estabelecimento_saude = database.Column('co_unidade', database.String(31))
    codigo_uf = database.Column('co_uf', database.Integer)
    codigo_ibge_municipio = database.Column('co_ibge', database.BigInteger)
    descricao_natureza_juridica_estabelecimento = database.Column('co_natureza_jur', database.String(14))
    codigo_motivo_desabilitacao_estabelecimento = database.Column('co_motivo_desab', database.String(2))
    estabelecimento_possui_centro_cirurgico = database.Column('st_centro_cirurgico', database.Integer)
    estabelecimento_possui_centro_obstetrico = database.Column('st_centro_obstetrico', database.Integer)
    estabelecimento_possui_centro_neonatal = database.Column('st_centro_neonatal', database.Integer)
    estabelecimento_possui_atendimento_hospitalar = database.Column('st_atend_hospitalar', database.Integer)
    estabelecimento_possui_servico_apoio = database.Column('st_servico_apoio', database.Integer)
    estabelecimento_possui_atendimento_ambulatorial = database.Column('st_atend_ambulatorial', database.Integer)
    codigo_atividade_ensino_unidade = database.Column('co_atividade', database.Integer)
    codigo_natureza_organizacao_unidade = database.Column('co_natureza_organizacao', database.Integer)
    codigo_nivel_hierarquia_unidade = database.Column('co_nivel_hierarquia', database.Integer)
    codigo_esfera_administrativa_unidade = database.Column('co_esfera_administrativa', database.Integer)

    def __init__(self,  codigo_cnes, numero_cnpj_entidade, nome_razao_social,  nome_fantasia,  natureza_organizacao_entidade,
            tipo_gestao, descricao_nivel_hierarquia, descricao_esfera_administrativa, codigo_tipo_unidade, codigo_cep_estabelecimento,
            endereco_estabelecimento, numero_estabelecimento, bairro_estabelecimento, numero_telefone_estabelecimento, 
            latitude_estabelecimento_decimo_grau, longitude_estabelecimento_decimo_grau, endereco_email_estabelecimento, numero_cnpj,
            codigo_identificador_turno_atendimento, descricao_turno_atendimento, estabelecimento_faz_atendimento_ambulatorial_sus,
            codigo_estabelecimento_saude, codigo_uf, codigo_ibge_municipio, descricao_natureza_juridica_estabelecimento,
            codigo_motivo_desabilitacao_estabelecimento, estabelecimento_possui_centro_cirurgico, estabelecimento_possui_centro_obstetrico,
            estabelecimento_possui_centro_neonatal, estabelecimento_possui_atendimento_hospitalar, estabelecimento_possui_servico_apoio,
            estabelecimento_possui_atendimento_ambulatorial, codigo_atividade_ensino_unidade, codigo_natureza_organizacao_unidade,
            codigo_nivel_hierarquia_unidade, codigo_esfera_administrativa_unidade):
        self.codigo_cnes = codigo_cnes
        self.numero_cnpj_entidade = numero_cnpj_entidade
        self.nome_razao_social = nome_razao_social
        self.nome_fantasia = nome_fantasia
        self.natureza_organizacao_entidade = natureza_organizacao_entidade
        self.tipo_gestao = tipo_gestao
        self.descricao_nivel_hierarquia = descricao_nivel_hierarquia
        self.descricao_esfera_administrativa = descricao_esfera_administrativa
        self.codigo_tipo_unidade = codigo_tipo_unidade
        self.codigo_cep_estabelecimento = codigo_cep_estabelecimento
        self.endereco_estabelecimento = endereco_estabelecimento
        self.numero_estabelecimento = numero_estabelecimento
        self.bairro_estabelecimento = bairro_estabelecimento
        self.numero_telefone_estabelecimento = numero_telefone_estabelecimento
        self.latitude_estabelecimento_decimo_grau = latitude_estabelecimento_decimo_grau
        self.longitude_estabelecimento_decimo_grau = longitude_estabelecimento_decimo_grau
        self.endereco_email_estabelecimento = endereco_email_estabelecimento
        self.numero_cnpj = numero_cnpj
        self.codigo_identificador_turno_atendimento = codigo_identificador_turno_atendimento
        self.descricao_turno_atendimento = descricao_turno_atendimento
        self.estabelecimento_faz_atendimento_ambulatorial_sus = estabelecimento_faz_atendimento_ambulatorial_sus
        self.codigo_estabelecimento_saude = codigo_estabelecimento_saude
        self.codigo_uf = codigo_uf
        self.codigo_ibge_municipio = codigo_ibge_municipio
        self.descricao_natureza_juridica_estabelecimento = descricao_natureza_juridica_estabelecimento
        self.codigo_motivo_desabilitacao_estabelecimento = codigo_motivo_desabilitacao_estabelecimento
        self.estabelecimento_possui_centro_cirurgico = estabelecimento_possui_centro_cirurgico
        self.estabelecimento_possui_centro_obstetrico = estabelecimento_possui_centro_obstetrico
        self.estabelecimento_possui_centro_neonatal = estabelecimento_possui_centro_neonatal
        self.estabelecimento_possui_atendimento_hospitalar = estabelecimento_possui_atendimento_hospitalar
        self.estabelecimento_possui_servico_apoio = estabelecimento_possui_servico_apoio
        self.estabelecimento_possui_atendimento_ambulatorial = estabelecimento_possui_atendimento_ambulatorial
        self.codigo_atividade_ensino_unidade = codigo_atividade_ensino_unidade
        self.codigo_natureza_organizacao_unidade = codigo_natureza_organizacao_unidade
        self.codigo_nivel_hierarquia_unidade = codigo_nivel_hierarquia_unidade
        self.codigo_esfera_administrativa_unidade = codigo_esfera_administrativa_unidade
    
    def json(self):
        return {
            'codigo_cnes': self.codigo_cnes,
            'numero_cnpj_entidade': self.numero_cnpj_entidade,
            'nome_razao_social': self.nome_razao_social,
            'nome_fantasia': self.nome_fantasia,
            'natureza_organizacao_entidade': self.natureza_organizacao_entidade,
            'tipo_gestao': self.tipo_gestao,
            'descricao_nivel_hierarquia': self.descricao_nivel_hierarquia,
            'descricao_esfera_administrativa': self.descricao_esfera_administrativa,
            'codigo_tipo_unidade': self.codigo_tipo_unidade,
            'codigo_cep_estabelecimento': self.codigo_cep_estabelecimento,
            'endereco_estabelecimento': self.endereco_estabelecimento,
            'numero_estabelecimento': self.numero_estabelecimento,
            'bairro_estabelecimento': self.bairro_estabelecimento,
            'numero_telefone_estabelecimento': self.numero_telefone_estabelecimento,
            'latitude_estabelecimento_decimo_grau': self.latitude_estabelecimento_decimo_grau,
            'longitude_estabelecimento_decimo_grau': self.longitude_estabelecimento_decimo_grau,
            'endereco_email_estabelecimento': self.endereco_email_estabelecimento,
            'numero_cnpj': self.numero_cnpj,
            'codigo_identificador_turno_atendimento': self.codigo_identificador_turno_atendimento,
            'descricao_turno_atendimento': self.descricao_turno_atendimento,
            'estabelecimento_faz_atendimento_ambulatorial_sus': self.estabelecimento_faz_atendimento_ambulatorial_sus,
            'codigo_estabelecimento_saude': self.codigo_estabelecimento_saude,
            'codigo_uf': self.codigo_uf,
            'codigo_ibge_municipio': self.codigo_ibge_municipio,
            'descricao_natureza_juridica_estabelecimento': self.descricao_natureza_juridica_estabelecimento,
            'codigo_motivo_desabilitacao_estabelecimento': self.codigo_motivo_desabilitacao_estabelecimento,
            'estabelecimento_possui_centro_cirurgico': self.estabelecimento_possui_centro_cirurgico,
            'estabelecimento_possui_centro_obstetrico': self.estabelecimento_possui_centro_obstetrico,
            'estabelecimento_possui_centro_neonatal': self.estabelecimento_possui_centro_neonatal,
            'estabelecimento_possui_atendimento_hospitalar': self.estabelecimento_possui_atendimento_hospitalar,
            'estabelecimento_possui_servico_apoio': self.estabelecimento_possui_servico_apoio,
            'estabelecimento_possui_atendimento_ambulatorial': self.estabelecimento_possui_atendimento_ambulatorial,
            'codigo_atividade_ensino_unidade': self.codigo_atividade_ensino_unidade,
            'codigo_natureza_organizacao_unidade': self.codigo_natureza_organizacao_unidade,
            'codigo_nivel_hierarquia_unidade': self.codigo_nivel_hierarquia_unidade,
            'codigo_esfera_administrativa_unidade': self.codigo_esfera_administrativa_unidade,
        }

    def find_estabelecimento(codigo_cnes):
        return EstabelecimentoModel.query.filter_by(codigo_cnes=codigo_cnes).first()

    def list_estabelecimentos(codigo_tipo_unidade=None,
                            estabelecimento_possui_centro_cirurgico=None,
                            estabelecimento_possui_centro_obstetrico=None,
                            limit=None,
                            offset=None,
                            **params):
        
        estabelecimentos = EstabelecimentoModel.query
        if codigo_tipo_unidade:
            print('tipo_unidade')
            estabelecimentos = estabelecimentos.filter_by(codigo_tipo_unidade=codigo_tipo_unidade)

        if estabelecimento_possui_centro_cirurgico is not None:
            print('cirurgico')
            estabelecimentos = estabelecimentos.filter_by(estabelecimento_possui_centro_cirurgico=estabelecimento_possui_centro_cirurgico)

        if estabelecimento_possui_centro_obstetrico is not None:
            print('obstetrico')
            estabelecimentos = estabelecimentos.filter_by(estabelecimento_possui_centro_obstetrico=estabelecimento_possui_centro_obstetrico)

        return estabelecimentos.limit(limit).offset(offset)
