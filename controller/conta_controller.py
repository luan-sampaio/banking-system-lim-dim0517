class ContaController:
    def __init__(self, conta_service, conta_poupanca_service):
        self.conta_service = conta_service
        self.conta_poupanca_service = conta_poupanca_service
        
    def cadastrar_conta(self):
        numero = input("         Numero da conta: ")
        
        try:
            conta = self.conta_service.cadastrar_conta(numero)
            return f"         Conta {conta.numero} Cadastrada com Sucesso!"
        except ValueError as erro:
            return f"\n         Erro: {erro}"

    def cadastrar_conta_bonus(self):
        numero = input("         Numero da conta bônus: ")

        try:
            conta = self.conta_service.cadastrar_conta_bonus(numero)
            return f"         Conta Bônus {conta.numero} Cadastrada com Sucesso! Pontuação: {conta.pontuacao}"
        except ValueError as erro:
            return f"\n         Erro: {erro}"

    def cadastrar_conta_poupanca(self):
        numero = input("         Numero da conta poupança: ")

        try:
            conta = self.conta_service.cadastrar_conta_poupanca(numero)
            return f"         Conta Poupança {conta.numero} Cadastrada com Sucesso!"
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
            conta = self.conta_service.validar_conta_ativa(numero)
            mensagem = f"         Saldo de {numero}: {saldo:.2f}"

            if hasattr(conta, "pontuacao"):
                mensagem += f"\n         Pontuação: {conta.pontuacao}"

            return mensagem

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
            conta_destino = self.conta_service.validar_conta_ativa(numero_destino)
            
            mensagem = f"\n         Saldo da conta de origem {numero_origem}: {saldo_origem:.2f}\n         Saldo da conta de destino {numero_destino}: {saldo_destino:.2f}"

            if hasattr(conta_destino, "pontuacao"):
                mensagem += f"\n         Pontuação da conta de destino: {conta_destino.pontuacao}"

            return mensagem

        except ValueError as erro:
            return f"\n         Erro: {erro}"

    def render_juros(self):
        taxa = input("         Taxa de juros: ")

        try:
            quantidade = self.conta_poupanca_service.render_juros_todas(taxa)
            return f"         Juros aplicados em {quantidade} conta(s) poupança."
        except ValueError as erro:
            return f"\n         Erro: {erro}"
