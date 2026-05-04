class ContaController:
    def __init__(self, conta_service):
        self.conta_service = conta_service
        
    def cadastrar_conta(self):
        numero = input("         Numero da conta: ")
        
        try:
            conta = self.conta_service.cadastrar_conta(numero)
            return f"         Conta {conta.numero} Cadastrada com Sucesso!"
        except ValueError as erro:
            return f"\n         Erro: {erro}"
    

    def consultar_saldo(self):
        numero = input("         Numero da conta: ")
        
        try:
            saldo = self.conta_service.consultar_saldo(numero)
            return f"         Saldo de {numero}: {saldo:.2f}"
        except ValueError as erro:
            return f"\n         Erro: {erro}"


    def creditar(self):
        numero = input("         Numero da conta: ")

        try:
            self.conta_service.validar_conta_ativa(numero)

            valor = input("         Valor do depósito: ")

            saldo = self.conta_service.creditar(numero, valor)
            return f"         Saldo de {numero}: {saldo:.2f}"

        except ValueError as erro:
            return f"\n         Erro: {erro}"