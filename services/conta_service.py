from decimal import Decimal, InvalidOperation

from models.conta import Conta
from models.conta_bonus import ContaBonus
from models.conta_poupanca import ContaPoupanca

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

    def cadastrar_conta_bonus(self, numero):
        if not numero.isdigit():
            raise ValueError("Valor não númerico ou negativo!")

        if self.conta_repository.buscar_conta(numero):
            raise ValueError("Conta Cadastrada com Esse Número!")

        conta = ContaBonus(numero)
        self.conta_repository.salvar_contas(conta)
        return conta

    def cadastrar_conta_poupanca(self, numero):
        if not numero.isdigit():
            raise ValueError("Valor não númerico ou negativo!")

        if self.conta_repository.buscar_conta(numero):
            raise ValueError("Conta Cadastrada com Esse Número!")

        conta = ContaPoupanca(numero)
        self.conta_repository.salvar_contas(conta)
        return conta
        
    def consultar_saldo(self, numero):
        if not numero.isdigit():
            raise ValueError("Valor não númerico ou negativo!")
                
        conta = self.conta_repository.buscar_conta(numero)
        
        if conta is None:
            raise ValueError("Não existe conta cadastrada com este número!")
        
        return conta.saldo
    
    def validar_conta_ativa(self, numero):
        if not numero.isdigit():
            raise ValueError("Valor não númerico ou negativo!")
                
        conta = self.conta_repository.buscar_conta(numero)

        if conta is None:
            raise ValueError("Não existe conta cadastrada com este número!")
        
        return conta

    def creditar(self, numero, valor):
        if not numero.isdigit():
            raise ValueError("Valor não númerico ou negativo!")
        
        conta = self.conta_repository.buscar_conta(numero)

        if conta is None:
            raise ValueError("Não existe conta cadastrada com este número!")
        
        valor_higienizado = valor.replace(",", ".")
        try:
            valor_decimal = Decimal(valor_higienizado)
        except InvalidOperation:
            raise ValueError("Formato monetário inválido. Digite um número válido (ex: 50.00).")
    
        if valor_decimal <= 0:
            raise ValueError("Valor de depósito deve ser maior que zero.")
        
        conta.saldo += valor_decimal

        if isinstance(conta, ContaBonus):
            conta.pontuacao += int(valor_decimal // Decimal("100"))

        self.conta_repository.salvar_contas(conta)
        return conta.saldo
    
    def debitar(self, numero, valor):
        if not numero.isdigit():
            raise ValueError("Valor não númerico ou negativo!")
        
        conta = self.conta_repository.buscar_conta(numero)

        if conta is None:
            raise ValueError("Não existe conta cadastrada com este número!")
        
        valor_higienizado = valor.replace(",", ".")
        try:
            valor_decimal = Decimal(valor_higienizado)
        except InvalidOperation:
            raise ValueError("Formato monetário inválido. Digite um número válido (ex: 50.00).")
        
        if valor_decimal <= 0:
            raise ValueError("Valor de depósito deve ser maior que zero.")
        
        if valor_decimal > conta.saldo:
            raise ValueError("Saldo insuficiente para esta operação.")

        conta.saldo -= valor_decimal
        self.conta_repository.salvar_contas(conta)
        return conta.saldo

    def transferir(self, numero_origem, numero_destino, valor):
        conta_origem = self.conta_repository.buscar_conta(numero_origem)
        conta_destino = self.conta_repository.buscar_conta(numero_destino)

        if conta_origem is None:
            raise ValueError("Não existe conta cadastrada com o número da conta de origem!")
        if conta_destino is None:
            raise ValueError("Não existe conta cadastrada com o número da conta de destino!")

        valor_higienizado = valor.replace(",", ".")
        try:
            valor_decimal = Decimal(valor_higienizado)
        except InvalidOperation:
            raise ValueError("Formato inválido. Digite um número válido.")
        
        if valor_decimal <= 0:
            raise ValueError("Valor de transferência deve ser maior que zero.")
        
        if valor_decimal > conta_origem.saldo:
            raise ValueError("Saldo insuficiente para esta operação.")
        
        conta_origem.saldo -= valor_decimal
        conta_destino.saldo += valor_decimal

        if isinstance(conta_destino, ContaBonus):
            conta_destino.pontuacao += int(valor_decimal // Decimal("200"))
        
        self.conta_repository.salvar_contas(conta_origem)
        self.conta_repository.salvar_contas(conta_destino)
        
        return conta_destino.saldo
