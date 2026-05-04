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
    
