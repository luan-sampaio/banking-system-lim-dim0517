class ContaRepository:
    def __init__(self):
        self.contas = {}

    def salvar_contas(self, conta):
        self.contas[conta.numero] = conta

    def buscar_conta(self, numero):
        return self.contas.get(numero)