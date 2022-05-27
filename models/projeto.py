from sql_alchemy import database

class IbgeModel(database.Model):
    __tablename__ = 'tb_ibge'
    __table_args__ = {'schema': 'dbgeral'}

    codigo_municipio = database.Column('codigo_ibge_txt', database.String(6), primary_key=True)
    municipio = database.Column('cidade', database.String(20))
    uf = database.Column('uf', database.String(2))


class ProjetoModel(database.Model):
    __tablename__ = 'tb_projeto'
    __table_args__ = {'schema': 'dbplataformabr'}

    codigo_sequencial_projeto = database.Column('co_seq_projeto', database.Integer(), primary_key=True)
    numero_caae = database.Column('nu_caae', database.String(20))
    titulo_projeto_pesquisa = database.Column('ds_titulo_publico', database.String())
    nome_comite_etica_pesquisa = database.Column('no_comite_etica', database.String(128))
    codigo_municipio_comite_etica_pesquisa = database.Column('co_municipio_ibge_cep', database.String(6))
    codigo_uf_comite_etica_pesquisa = database.Column('co_uf_ibge_cep', database.String(2))
    data_submissao_projeto_pesquisa = database.Column('dt_primeira_submissao', database.Date())
    numero_parecer  = database.Column('co_seq_parecer', database.Numeric(scale=15))
    data_submissao_ultima_versao_projeto_pesquisa = database.Column('dt_submissao', database.Date())
    data_emissao_parecer = database.Column('dt_parecer', database.Date())
    situação_parecer = database.Column('st_parecer', database.String(50))
    nome_instituicao_proponente = database.Column('no_instituicao', database.String(250))
    codigo_municipio_instituicao_proponente = database.Column('co_municipio_ibge_instituicao', database.String(6))
    codigo_uf_instituicao_proponente = database.Column('sg_uf_instituicao', database.String(2))

    def __init__(self, numero_caae, titulo_projeto_pesquisa, nome_comite_etica_pesquisa,
        codigo_municipio_comite_etica_pesquisa, codigo_uf_comite_etica_pesquisa,
        data_submissao_projeto_pesquisa, numero_parecer, data_submissao_ultima_versao_projeto_pesquisa,
        data_emissao_parecer, situação_parecer, nome_instituicao_proponente, codigo_municipio_instituicao_proponente,
        codigo_uf_instituicao_proponente):
        self.numero_caae = numero_caae
        self.titulo_projeto_pesquisa = titulo_projeto_pesquisa
        self.nome_comite_etica_pesquisa = nome_comite_etica_pesquisa
        self.codigo_municipio_comite_etica_pesquisa = codigo_municipio_comite_etica_pesquisa
        self.codigo_uf_comite_etica_pesquisa = codigo_uf_comite_etica_pesquisa
        self.data_submissao_projeto_pesquisa = data_submissao_projeto_pesquisa
        self.numero_parecer  = numero_parecer 
        self.data_submissao_ultima_versao_projeto_pesquisa = data_submissao_ultima_versao_projeto_pesquisa
        self.data_emissao_parecer = data_emissao_parecer
        self.situação_parecer = situação_parecer
        self.nome_instituicao_proponente = nome_instituicao_proponente
        self.codigo_municipio_instituicao_proponente = codigo_municipio_instituicao_proponente
        self.codigo_uf_instituicao_proponente = codigo_uf_instituicao_proponente
        
    def json(self):
        return {
            'numero_caae': self.numero_caae,
            'titulo_projeto_pesquisa': self.titulo_projeto_pesquisa,
            'nome_comite_etica_pesquisa': self.nome_comite_etica_pesquisa,
            'codigo_municipio_comite_etica_pesquisa': self.codigo_municipio_comite_etica_pesquisa,
            'codigo_uf_comite_etica_pesquisa': self.codigo_uf_comite_etica_pesquisa,
            'data_submissao_projeto_pesquisa': self.data_submissao_projeto_pesquisa.strftime('%Y-%m-%d'),
            'numero_parecer ': float(self.numero_parecer),
            'data_submissao_ultima_versao_projeto_pesquisa': self.data_submissao_ultima_versao_projeto_pesquisa.strftime('%Y-%m-%d'),
            'data_emissao_parecer': self.data_emissao_parecer.strftime('%Y-%m-%d'),
            'situacao_parecer': self.situação_parecer,
            'nome_instituicao_proponente': self.nome_instituicao_proponente,
            'codigo_municipio_instituicao_proponente': self.codigo_municipio_instituicao_proponente,
            'codigo_uf_instituicao_proponente': self.codigo_uf_instituicao_proponente
        }

    def find_projeto(codigo_sequencial_projeto):
        return ProjetoModel.query.filter_by(codigo_sequencial_projeto=codigo_sequencial_projeto).first()


    def list_projetos():
        return ProjetoModel.query.all()