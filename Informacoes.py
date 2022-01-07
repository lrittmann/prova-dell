class Informacoes():
    def __init__(self, data_extracao, id_usuario, situacao, central_regulacao_origem, data_solicitacao, sexo, idade, municipio_residencia, solicitante, municipio_solicitante, codigo_cid, carater, tipo_internacao, tipo_leito, data_autorizacao, data_internacao, data_alta, executante, horas_na_fila ):
        self.data_extracao = data_extracao
        self.id_usuario = id_usuario
        self.situacao = situacao
        self.central_regulacao_origem = central_regulacao_origem
        self.data_solicitacao = data_solicitacao
        self.sexo = sexo
        self.idade = idade
        self.municipio_residencia = municipio_residencia
        self.solicitante = solicitante
        self.municipio_solicitante = municipio_solicitante
        self.codigo_cid = codigo_cid
        self.carater = carater
        self.tipo_internacao = tipo_internacao
        self.tipo_leito = tipo_leito
        self.data_autorizacao = data_autorizacao
        self.data_internacao = data_internacao
        self.data_alta = data_alta
        self.executante = executante
        self.horas_na_fila = horas_na_fila
    
    def get_data_extracao(self):
        return self.data_extracao
    
    def get_id_usuario(self):
        return self.id_usuario

    def get_situacao(self):
        return self.situacao

    def get_central_regulacao_origem(self):
        return self.central_regulacao_origem

    def get_data_solicitacao(self):
        return self.data_solicitacao

    def get_sexo(self):
        return self.sexo

    def get_idade(self):
        return self.idade

    def get_municipio_residencia(self):
        return self.municipio_residencia

    def get_solicitante(self):
        return self.solicitante

    def get_municipio_solicitante(self):
        return self.municipio_solicitante

    def get_codigo_cid(self):
        return self.codigo_cid

    def get_carater(self):
        return self.carater

    def get_tipo_internacao(self):
        return self.tipo_internacao

    def get_tipo_leito(self):
        return self.tipo_leito

    def get_data_autorizacao(self):
        return self.data_autorizacao

    def get_data_internacao(self):
        return self.data_internacao

    def get_data_alta(self):
        return self.data_alta

    def get_executante(self):
        return self.executante

    def get_horas_na_fila(self):
        return self.horas_na_fila

    def ToString(self):
        return ("Data extracao: " + self.get_data_extracao(), "ID do usuario: " + self.get_id_usuario(), "Situacao: " + self.get_situacao(),"Central de Regulacao: " +  self.get_central_regulacao_origem(),"Data de Solicitacao: " + self.get_data_solicitacao(),"Sexo: " +  self.get_sexo(),"Idade: " +  self.get_idade(),"Municipio Residente: " +  self.get_municipio_residencia(),"Solicitante: " +  self.get_solicitante(), "Municipio Solicitante: " +  self.get_municipio_solicitante(),"Codigo Cidadao: "+   self.get_codigo_cid(),"Carater: " + self.get_carater(),"Tipo Internacao: " +  self.get_tipo_internacao(),"Tipo de Leito: " +  self.get_tipo_leito(),"Data de Autorizacao: " +  self.get_data_autorizacao(),"Data Internacao: " +  self.get_data_internacao(),"Data Alta: " +  self.get_data_alta(),"Executante: " +  self.get_executante(), "Horas na Fila: " + self.get_horas_na_fila())