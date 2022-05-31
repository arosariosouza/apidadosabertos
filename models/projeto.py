from sql_alchemy import database
from sqlalchemy import func


class ProjetoModel(database.Model):
    __tablename__ = 'vw_projeto_ibge'
    __table_args__ = {'schema': 'dbplataformabr'}

    numero_caae = database.Column('nu_caae', database.String(), primary_key=True)
    titulo_projeto_pesquisa = database.Column('ds_titulo_publico', database.String())
    nome_comite_etica_pesquisa = database.Column('no_comite_etica', database.String(128))
    municipio_comite_etica_pesquisa = database.Column('municipio_comite_etica', database.String(70))
    uf_comite_etica_pesquisa = database.Column('uf_comite_etica', database.String(2))
    data_submissao_projeto_pesquisa = database.Column('dt_primeira_submissao', database.Date())
    numero_parecer  = database.Column('co_seq_parecer', database.Numeric(scale=15))
    data_submissao_ultima_versao_projeto_pesquisa = database.Column('dt_submissao', database.Date())
    data_emissao_parecer = database.Column('dt_parecer', database.Date())
    codigo_situacao_parecer = database.Column('co_st_parecer', database.Integer())
    situacao_parecer = database.Column('st_parecer', database.String(50))
    nome_instituicao_proponente = database.Column('no_instituicao', database.String(250))
    municipio_instituicao_proponente = database.Column('municipio_instituicao', database.String(70))
    uf_instituicao_proponente = database.Column('sg_uf_instituicao', database.String(2))

    def __init__(self, numero_caae, titulo_projeto_pesquisa,
        nome_comite_etica_pesquisa, municipio_comite_etica_pesquisa, uf_comite_etica_pesquisa,
        data_submissao_projeto_pesquisa, numero_parecer, data_submissao_ultima_versao_projeto_pesquisa,
        data_emissao_parecer, codigo_situacao_parecer, situacao_parecer, nome_instituicao_proponente,
        municipio_instituicao_proponente, uf_instituicao_proponente):
        self.numero_caae = numero_caae
        self.titulo_projeto_pesquisa = titulo_projeto_pesquisa
        self.nome_comite_etica_pesquisa = nome_comite_etica_pesquisa
        self.municipio_comite_etica_pesquisa = municipio_comite_etica_pesquisa
        self.uf_comite_etica_pesquisa = uf_comite_etica_pesquisa
        self.data_submissao_projeto_pesquisa = data_submissao_projeto_pesquisa
        self.numero_parecer  = numero_parecer 
        self.data_submissao_ultima_versao_projeto_pesquisa = data_submissao_ultima_versao_projeto_pesquisa
        self.data_emissao_parecer = data_emissao_parecer,
        self.codigo_situacao_parecer = codigo_situacao_parecer,
        self.situacao_parecer = situacao_parecer
        self.nome_instituicao_proponente = nome_instituicao_proponente
        self.municipio_instituicao_proponente = municipio_instituicao_proponente
        self.uf_instituicao_proponente = uf_instituicao_proponente
       
    def json(self):
        return {
            'numero_caae': self.numero_caae,
            'titulo_projeto_pesquisa': self.titulo_projeto_pesquisa,
            'nome_comite_etica_pesquisa': self.nome_comite_etica_pesquisa,
            'municipio_comite_etica_pesquisa': self.municipio_comite_etica_pesquisa,
            'uf_comite_etica_pesquisa': self.uf_comite_etica_pesquisa,
            'data_submissao_projeto_pesquisa': self.data_submissao_projeto_pesquisa.strftime('%Y-%m-%d'),
            'numero_parecer ': float(self.numero_parecer),
            'data_submissao_ultima_versao_projeto_pesquisa': self.data_submissao_ultima_versao_projeto_pesquisa.strftime('%Y-%m-%d'),
            'data_emissao_parecer': self.data_emissao_parecer.strftime('%Y-%m-%d'),
            'situacao_parecer': self.situacao_parecer,
            'nome_instituicao_proponente': self.nome_instituicao_proponente,
            'municipio_instituicao_proponente': self.municipio_instituicao_proponente,
            'uf_instituicao_proponente': self.uf_instituicao_proponente
        }

    def find_projeto(numero_caae):
        p = ProjetoModel.query.filter_by(numero_caae=numero_caae).first()
        return p

    def list_projetos(uf_comite_etica_pesquisa=None,
                            codigo_situacao_parecer=None,
                            uf_instituicao_proponente=None,
                            limit=None,
                            offset=None,
                            **params):
        
        projetos = ProjetoModel.query
        if uf_comite_etica_pesquisa is not None:
            projetos = projetos.filter(func.lower(ProjetoModel.uf_comite_etica_pesquisa) == func.lower(uf_comite_etica_pesquisa))

        if codigo_situacao_parecer is not None:
            projetos = projetos.filter_by(codigo_situacao_parecer=codigo_situacao_parecer)

        if uf_instituicao_proponente is not None:
            projetos = projetos.filter(func.lower(ProjetoModel.uf_instituicao_proponente) == func.lower(uf_instituicao_proponente))

        return projetos.limit(limit).offset(offset)