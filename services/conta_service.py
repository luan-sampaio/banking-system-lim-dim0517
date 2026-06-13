from decimal import Decimal

from models.conta import Conta
from models.conta_bonus import ContaBonus
from models.conta_poupanca import ContaPoupanca


class ContaService:
    def __init__(self, conta_repository):
        self.conta_repository = conta_repository

    def _validar_numero(self, numero, mensagem="valor não numérico ou negativo."):
        if not numero.isdigit():
            raise ValueError(mensagem)

    def _validar_nao_existente(self, numero):
        if self.conta_repository.buscar_conta(numero):
            raise ValueError("Já existe uma conta cadastrada com este número!")

    def _validar_valor_positivo(self, valor, mensagem="Valor deve ser maior que zero."):
        if valor <= 0:
            raise ValueError(mensagem)

    def _validar_nao_negativo(self, valor, mensagem="Valor não pode ser negativo."):
        if valor < 0:
            raise ValueError(mensagem)

    def buscar_conta(self, numero):
        self._validar_numero(numero, "O número da conta deve conter apenas dígitos.")
        conta = self.conta_repository.buscar_conta(numero)
        
        if conta is None:
            raise ValueError("Não existe conta cadastrada com este número!")
        
        return conta

    def cadastrar_conta(self, numero, saldo_inicial=Decimal("0")):
        self._validar_numero(numero, "O número da conta deve conter apenas dígitos.")
        self._validar_nao_existente(numero)
        self._validar_numero(saldo_inicial, "O saldo inicial deve ser um valor numérico válido.")
        saldo_Decimal = Decimal(saldo_inicial)
        self._validar_nao_negativo(saldo_Decimal, "Saldo inicial não pode ser negativo.")
        
        conta = Conta(numero, saldo_Decimal)
        
        self.conta_repository.salvar_contas(conta)
        
        return conta

    def cadastrar_conta_bonus(self, numero):
        self._validar_numero(numero, "O número da conta deve conter apenas dígitos.")
        self._validar_nao_existente(numero)
        
        conta = ContaBonus(numero)
        
        self.conta_repository.salvar_contas(conta)
        
        return conta

    def cadastrar_conta_poupanca(self, numero, saldo_inicial):
        self._validar_numero(numero, "O número da conta deve conter apenas dígitos.")
        self._validar_nao_existente(numero)
        self._validar_numero(saldo_inicial, "O saldo inicial deve ser um valor numérico válido.")
        saldo_Decimal = Decimal(saldo_inicial)
        self._validar_nao_negativo(saldo_Decimal, "O saldo inicial não pode ser negativo.")
        
        conta = ContaPoupanca(numero, saldo_Decimal)
        
        self.conta_repository.salvar_contas(conta)
        
        return conta

    def consultar_saldo(self, numero):
        conta = self.buscar_conta(numero)
        
        return conta.saldo

    def creditar(self, numero, valor):
        conta = self.buscar_conta(numero)
        self._validar_numero(valor, "O valor de depósito deve ser um valor numérico válido e maior que zero.")
        valor_decimal = Decimal(valor)
        self._validar_valor_positivo(valor_decimal, "O valor de depósito deve ser maior que zero.")
        
        conta.saldo += valor_decimal
        
        if isinstance(conta, ContaBonus):
            conta.pontuacao += int(valor_decimal // Decimal("150"))
        self.conta_repository.salvar_contas(conta)
        return conta.saldo

    def debitar(self, numero, valor):
        conta = self.buscar_conta(numero)
        self._validar_numero(valor, "O valor de saque deve ser um valor numérico válido e maior que zero.")
        valor_decimal = Decimal(valor)
        self._validar_valor_positivo(valor_decimal, "O valor de saque deve ser maior que zero.")
        
        if valor_decimal > conta.saldo:
            raise ValueError("Saldo insuficiente para esta operação.")
        
        conta.saldo -= valor_decimal
        self.conta_repository.salvar_contas(conta)
        
        return conta.saldo

    def transferir(self, numero_origem, numero_destino, valor):
        conta_origem = self.buscar_conta(numero_origem)
        conta_destino = self.buscar_conta(numero_destino)

        self._validar_numero(valor, "O valor de transferência deve ser um valor numérico válido e maior que zero.")
        valor_decimal = Decimal(valor)
        self._validar_valor_positivo(valor_decimal, "O valor de transferência deve ser maior que zero.")
        
        if valor_decimal > conta_origem.saldo:
            raise ValueError("Saldo insuficiente para esta operação.")
        
        conta_origem.saldo -= valor_decimal
        conta_destino.saldo += valor_decimal
        
        if isinstance(conta_destino, ContaBonus):
            conta_destino.pontuacao += int(valor_decimal // Decimal("200"))
        
        self.conta_repository.salvar_contas(conta_origem)
        self.conta_repository.salvar_contas(conta_destino)
        
        return conta_destino.saldo

    def consultar_dados(self, numero):
        self._validar_numero(numero, "O número da conta deve conter apenas dígitos.")
        conta = self.buscar_conta(numero)
        
        dados_conta = {}
        
        if isinstance(conta, ContaBonus):
            dados_conta['tipo'] = 'Conta Bônus'
            dados_conta['pontuacao'] = conta.pontuacao
        elif isinstance(conta, ContaPoupanca):
            dados_conta['tipo'] = 'Conta Poupança'
            dados_conta['pontuacao'] = 'Não possui'
        else:
            dados_conta['tipo'] = 'Conta Normal'
            dados_conta['pontuacao'] = 'Não possui'
        
        dados_conta['numero'] = numero
        dados_conta['saldo'] = float(f"{conta.saldo:.2f}")
        
        return dados_conta
