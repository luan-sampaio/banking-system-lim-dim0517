import os
from decimal import Decimal, InvalidOperation


class ContaController:
    def __init__(self, conta_service, conta_poupanca_service):
        self.conta_service = conta_service
        self.conta_poupanca_service = conta_poupanca_service

    def _parse_decimal(self, valor_str, mensagem_erro="Formato monetário inválido."):
        valor_higienizado = valor_str.replace(",", ".")
        try:
            return Decimal(valor_higienizado)
        except InvalidOperation:
            raise ValueError(mensagem_erro)

    def cadastrar_conta(self):
        numero = input("         Numero da conta: ")
        saldo_inicial_str = input("         Saldo inicial: ")

        try:
            saldo_inicial = self._parse_decimal(saldo_inicial_str, "Formato monetário inválido para saldo inicial.") if saldo_inicial_str else Decimal("0")
            conta = self.conta_service.cadastrar_conta(numero, saldo_inicial)
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
        saldo_inicial_str = input("         Saldo inicial (R$): ")

        try:
            saldo_inicial = self._parse_decimal(saldo_inicial_str)
            conta = self.conta_service.cadastrar_conta_poupanca(numero, saldo_inicial)
            return f"         Conta Poupança {conta.numero} Cadastrada com Sucesso! Saldo Inicial: R$ {conta.saldo:.2f}"
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
            valor_str = input("         Valor do depósito: ")
            valor = self._parse_decimal(valor_str)

            saldo = self.conta_service.creditar(numero, valor)
            conta = self.conta_service.buscar_conta(numero)
            mensagem = f"         Saldo de {numero}: {saldo:.2f}"

            if hasattr(conta, "pontuacao"):
                mensagem += f"\n         Pontuação: {conta.pontuacao}"

            return mensagem

        except ValueError as erro:
            return f"\n         Erro: {erro}"


    def debitar(self):
        numero = input("         Numero da conta: ")

        try:
            valor_str = input("         Valor da retirada: ")
            valor = self._parse_decimal(valor_str)

            saldo = self.conta_service.debitar(numero, valor)
            return f"         Saldo de {numero}: {saldo:.2f}"

        except ValueError as erro:
            return f"\n         Erro: {erro}"

    def transferir(self):
        numero_origem = input("         Numero da conta de origem: ")
        numero_destino = input("         Numero da conta de destino: ")
        valor_str = input("         Valor da transferência: ")

        try:
            valor = self._parse_decimal(valor_str)
            self.conta_service.transferir(numero_origem, numero_destino, valor)

            saldo_origem = self.conta_service.consultar_saldo(numero_origem)
            saldo_destino = self.conta_service.consultar_saldo(numero_destino)
            conta_destino = self.conta_service.buscar_conta(numero_destino)

            mensagem = f"\n         Saldo da conta de origem {numero_origem}: {saldo_origem:.2f}\n         Saldo da conta de destino {numero_destino}: {saldo_destino:.2f}"

            if hasattr(conta_destino, "pontuacao"):
                mensagem += f"\n         Pontuação da conta de destino: {conta_destino.pontuacao}"

            return mensagem

        try:
            quantidade = self.conta_poupanca_service.render_juros_todas(taxa)
            return f"         Juros aplicados em {quantidade} conta(s) poupança."
        except ValueError as erro:
            return f"\n         Erro: {erro}"

    def render_juros(self):
        taxa_str = input("         Taxa de juros: ")

        try:
            taxa = self._parse_decimal(taxa_str, "Formato inválido. Digite uma taxa válida.")
            quantidade = self.conta_poupanca_service.render_juros_todas(taxa)
            return f"         Juros aplicados em {quantidade} conta(s) poupança."
        except ValueError as erro:
            return f"\n         Erro: {erro}"

    def consultar_dados(self):
        numero = input("         Numero da conta: ")

        try:
            dados_conta = self.conta_service.consultar_dados(numero)
            os.system("cls" if os.name == "nt" else "clear")
            print("========== Banking System L.I.M. ==========\n")

            return (
                "         Dados da conta: \n\n"
                f"         Tipo: {dados_conta['tipo']}\n"
                f"         Número: {dados_conta['numero']}\n"
                f"         Saldo: {dados_conta['saldo']:.2f}\n"
                f"         Bônus: {dados_conta['pontuacao']}\n"

            )
        except ValueError as erro:
            return f"\n         Erro: {erro}"
