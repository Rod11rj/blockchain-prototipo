import hashlib
import datetime

class Bloco():
    def __init__(self, indice, ultimo_hash, usuario, msg):
        self.indice = indice
        self.ultimo_hash = ultimo_hash
        self.usuario = usuario
        self.msg = msg
        self.datahora = datetime.datetime.now()
        self.hash = self.calcula_hash()

    def calcula_hash(self):
        dados_concatenados = str(self.datahora) + str(self.indice)  + str(self.ultimo_hash) + str(self.msg)
        return hashlib.sha256(dados_concatenados.encode()).hexdigest()

class Blockchain:
    def __init__(self, usuario):
        self.corrente = [self.cria_bloco_genesis(usuario)]
        self.usuario = usuario
        self.msg = ''

    def cria_bloco_genesis(self, usuario):
        return Bloco(0,'0', usuario, 'Comunicacao Baseada Em Blockchain: Chat Iniciado')

    def adiciona_bloco(self,msg):
        indice = len(self.corrente)
        ultimo_hash = self.corrente[-1].hash
        novo_bloco = Bloco(indice, ultimo_hash, self.usuario, msg)
        self.corrente.append(novo_bloco)

    def verifica_validade_bloco(self):
        for i in range(1,len(self.corrente)):
            bloco_atual = self.corrente[i]
            bloco_anterior = self.corrente[i-1]

            if bloco_atual.hash != bloco_atual.calcula_hash():
                return False
            elif bloco_atual.ultimo_hash != bloco_anterior.calcula_hash():
                return False

        return True

    def le_msg(self):
        return self.msg
