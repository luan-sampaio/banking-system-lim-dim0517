from decimal import Decimal


class Conta:
    def __init__(self, numero):
        self.numero = numero
        self.saldo = Decimal('0')
