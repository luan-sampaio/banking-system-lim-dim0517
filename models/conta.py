from decimal import Decimal


class Conta:
    def __init__(self, numero, saldo_inicial="0"):
        self.numero = numero
        self.saldo = Decimal(saldo_inicial)
