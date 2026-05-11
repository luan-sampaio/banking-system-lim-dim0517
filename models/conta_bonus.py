from models.conta import Conta


class ContaBonus(Conta):
    def __init__(self, numero):
        super().__init__(numero)
        self.pontuacao = 10
