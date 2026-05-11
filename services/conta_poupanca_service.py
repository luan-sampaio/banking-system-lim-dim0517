from decimal import Decimal, InvalidOperation

from models.conta_poupanca import ContaPoupanca


class ContaPoupancaService:
    def __init__(self, conta_repository):
        self.conta_repository = conta_repository

    def render_juros_todas(self, taxa):
        taxa_decimal = self._validar_taxa(taxa)
        contas_poupanca = [
            conta
            for conta in self.conta_repository.listar_contas()
            if isinstance(conta, ContaPoupanca)
        ]

        for conta in contas_poupanca:
            conta.saldo += conta.saldo * taxa_decimal / Decimal("100")
            self.conta_repository.salvar_contas(conta)

        return len(contas_poupanca)

    def _validar_taxa(self, taxa):
        taxa_higienizada = taxa.replace(",", ".")

        try:
            taxa_decimal = Decimal(taxa_higienizada)
        except InvalidOperation:
            raise ValueError("Formato inválido. Digite uma taxa válida.")

        if taxa_decimal <= 0:
            raise ValueError("Taxa de juros deve ser maior que zero.")

        return taxa_decimal
