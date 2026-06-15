from decimal import Decimal

from models.conta_poupanca import ContaPoupanca


class ContaPoupancaService:
    def __init__(self, conta_repository):
        self.conta_repository = conta_repository
    
    def _validar_valor(self, numero, mensagem="valor não numérico, igual a zero ou negativo."):
        try:
            valor = float(numero)
        except ValueError:
            raise ValueError(mensagem)
    
        if valor <= 0:
            raise ValueError(mensagem)
    
    def _validar_valor_positivo(self, valor, mensagem="Valor deve ser maior que zero."):
        if valor <= 0:
            raise ValueError(mensagem)   

    def render_juros_todas(self, taxa):

        self._validar_valor(taxa, "A taxa de juros deve ser um valor numérico válido.")
        taxa_decimal = Decimal(taxa)
        self._validar_valor_positivo(taxa_decimal, "A taxa de juros deve ser um valor maior que zero.")

        contas_poupanca = [
            conta
            for conta in self.conta_repository.listar_contas()
            if isinstance(conta, ContaPoupanca)
        ]

        for conta in contas_poupanca:
            conta.saldo += conta.saldo * taxa_decimal / Decimal("100")
            self.conta_repository.salvar_contas(conta)

        return len(contas_poupanca)
