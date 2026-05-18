from models.conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero):
        super().__init__(numero)
