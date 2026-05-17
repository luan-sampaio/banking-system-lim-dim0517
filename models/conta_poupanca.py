from decimal import Decimal
from models.conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero, saldo_inicial=Decimal('0')):
        super().__init__(numero)
        self.saldo = saldo_inicial
