import pytest
from decimal import Decimal

from models.conta import Conta
from models.conta_bonus import ContaBonus
from models.conta_poupanca import ContaPoupanca
from repositories.conta_repository import ContaRepository
from services.conta_service import ContaService


@pytest.fixture
def repository():
    return ContaRepository()


@pytest.fixture
def service(repository):
    return ContaService(repository)


class TestCadastrarConta:
    def test_cadastrar_conta_normal_com_sucesso(self, service):
        conta = service.cadastrar_conta("1", Decimal("100"))
        assert isinstance(conta, Conta)
        assert conta.numero == "1"
        assert conta.saldo == Decimal("100")

    def test_cadastrar_conta_normal_sem_saldo(self, service):
        with pytest.raises(ValueError, match="deve ser um valor numérico válido"):
            service.cadastrar_conta("2")

    def test_cadastrar_conta_normal_com_numero_invalido(self, service):
        with pytest.raises(ValueError, match="deve conter apenas dígitos"):
            service.cadastrar_conta("abc", Decimal("100"))

    def test_cadastrar_conta_normal_com_numero_vazio(self, service):
        with pytest.raises(ValueError, match="deve conter apenas dígitos"):
            service.cadastrar_conta("", Decimal("100"))

    def test_cadastrar_conta_normal_com_numero_duplicado(self, service):
        service.cadastrar_conta("3", Decimal("100"))
        with pytest.raises(ValueError, match="Já existe uma conta cadastrada"):
            service.cadastrar_conta("3", Decimal("200"))

    def test_cadastrar_conta_normal_saldo_negativo(self, service):
        with pytest.raises(ValueError, match="deve ser um valor numérico válido"):
            service.cadastrar_conta("4", Decimal("-50"))

    def test_cadastrar_conta_normal_saldo_zero(self, service):
        with pytest.raises(ValueError, match="deve ser um valor numérico válido"):
            service.cadastrar_conta("5", "0")

    def test_cadastrar_conta_normal_saldo_invalido(self, service):
        with pytest.raises(ValueError, match="deve ser um valor numérico"):
            service.cadastrar_conta("6", "abc")


class TestCadastrarContaBonus:
    def test_cadastrar_conta_bonus_com_sucesso(self, service):
        conta = service.cadastrar_conta_bonus("1")
        assert isinstance(conta, ContaBonus)
        assert conta.numero == "1"
        assert conta.saldo == Decimal("0")
        assert conta.pontuacao == 10

    def test_cadastrar_conta_bonus_numero_invalido(self, service):
        with pytest.raises(ValueError, match="deve conter apenas dígitos"):
            service.cadastrar_conta_bonus("abc")

    def test_cadastrar_conta_bonus_numero_duplicado(self, service):
        service.cadastrar_conta_bonus("2")
        with pytest.raises(ValueError, match="Já existe uma conta cadastrada"):
            service.cadastrar_conta_bonus("2")

    def test_cadastrar_conta_bonus_sem_saldo(self, service):
        with pytest.raises(ValueError, match="deve ser um valor numérico válido"):
            service.cadastrar_conta_poupanca("3", "0")
    
    def test_cadastrar_conta_bonus_saldo_negativo(self, service):
        with pytest.raises(ValueError, match="deve ser um valor numérico válido"):
            service.cadastrar_conta_poupanca("4", Decimal("-1"))

    def test_cadastrar_conta_bonus_saldo_invalido(self, service):
        with pytest.raises(ValueError, match="deve ser um valor numérico"):
            service.cadastrar_conta_poupanca("5", "xyz")


class TestCadastrarContaPoupanca:
    def test_cadastrar_conta_poupanca_com_sucesso(self, service):
        conta = service.cadastrar_conta_poupanca("1", Decimal("200"))
        assert isinstance(conta, ContaPoupanca)
        assert conta.numero == "1"
        assert conta.saldo == Decimal("200")

    def test_cadastrar_conta_poupanca_sem_saldo(self, service):
        with pytest.raises(ValueError, match="deve ser um valor numérico válido"):
            service.cadastrar_conta_poupanca("2", "0")

    def test_cadastrar_conta_poupanca_numero_invalido(self, service):
        with pytest.raises(ValueError, match="deve conter apenas dígitos"):
            service.cadastrar_conta_poupanca("abc", Decimal("100"))

    def test_cadastrar_conta_poupanca_numero_duplicado(self, service):
        service.cadastrar_conta_poupanca("3", Decimal("100"))
        with pytest.raises(ValueError, match="Já existe uma conta cadastrada"):
            service.cadastrar_conta_poupanca("3", Decimal("200"))

    def test_cadastrar_conta_poupanca_saldo_negativo(self, service):
        with pytest.raises(ValueError, match="deve ser um valor numérico válido"):
            service.cadastrar_conta_poupanca("4", Decimal("-1"))

    def test_cadastrar_conta_poupanca_saldo_invalido(self, service):
        with pytest.raises(ValueError, match="deve ser um valor numérico"):
            service.cadastrar_conta_poupanca("5", "xyz")
