from models.conta import Conta

class ContaService:
    def __init__(self, conta_repository):
        self.conta_repository = conta_repository
        
    def cadastrar_conta(self, numero):    
        if not numero.isdigit():
            raise ValueError("Valor não númerico ou negativo!")
                
        
        if self.conta_repository.buscar_conta(numero):
            raise ValueError("Conta Cadastrada com Esse Número!")

        
        conta = Conta(numero)
        self.conta_repository.salvar_contas(conta)
        return conta
        
    def consultar_saldo(self, numero):
        if not numero.isdigit():
            raise ValueError("Valor não númerico ou negativo!")
                
        conta = self.conta_repository.buscar_conta(numero)
        
        if conta is None:
            raise ValueError("Não existe conta cadastrada com este número!")
        
        return conta.saldo
