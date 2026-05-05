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
        

    def debitar(self):
        numero = input("         Numero da conta: ")

        try:
            self.conta_service.validar_conta_ativa(numero)

            valor = input("         Valor da retirada: ")

            saldo = self.conta_service.debitar(numero, valor)
            return f"         Saldo de {numero}: {saldo:.2f}"

        except ValueError as erro:
            return f"\n         Erro: {erro}"

    def transferir(self):
        numero_origem = input("         Numero da conta de origem: ")
        numero_destino = input("         Numero da conta de destino: ")
        valor = input("         Valor da transferência: ")

        try:
            self.conta_service.transferir(numero_origem, numero_destino, valor)
            
            saldo_origem = self.conta_service.consultar_saldo(numero_origem)
            saldo_destino = self.conta_service.consultar_saldo(numero_destino)
            
            return f"         \nSaldo da conta de origem {numero_origem}: {saldo_origem:.2f}\n         Saldo da conta de destino {numero_destino}: {saldo_destino:.2f}"

        except ValueError as erro:
            return f"\n         Erro: {erro}"