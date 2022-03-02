from sql_alchemy import database


class TipoUnidadeModel(database.Model):
    __tablename__ = 'tb_cnes_tipo_unidade'
    __table_args__ = {'schema': 'dbacoes_saude'}


    codigo_tipo_unidade = database.Column('co_tipo_unidade', database.BigInteger, primary_key=True)
    descricao_tipo_unidade = database.Column('ds_tipo_unidade', database.String(255))

    def __init__(self, codigo_tipo_unidade, descricao_tipo_unidade):
        self.codigo_tipo_unidade = codigo_tipo_unidade
        self.descricao_tipo_uniade = descricao_tipo_unidade

    def json(self):
        return {
            'codigo_tipo_unidade': self.codigo_tipo_unidade,
            'descricao_tipo_unidade': self.descricao_tipo_unidade 
        }

    def find_tipo_unidade(codigo_tipo_unidade):
        return TipoUnidadeModel.query.filter_by(codigo_tipo_unidade=codigo_tipo_unidade).first()


    def list_tipo_unidades():
        return TipoUnidadeModel.query.all()
