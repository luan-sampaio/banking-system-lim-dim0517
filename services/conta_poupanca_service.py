from decimal import Decimal

from models.conta_poupanca import ContaPoupanca


class ContaPoupancaService:
    def __init__(self, conta_repository):
        self.conta_repository = conta_repository

    def render_juros_todas(self, taxa):
        if taxa <= 0:
            raise ValueError("Taxa de juros deve ser maior que zero.")

        contas_poupanca = [
            conta
            for conta in self.conta_repository.listar_contas()
            if isinstance(conta, ContaPoupanca)
        ]

        for conta in contas_poupanca:
            conta.saldo += conta.saldo * taxa / Decimal("100")
            self.conta_repository.salvar_contas(conta)

        return len(contas_poupanca)
