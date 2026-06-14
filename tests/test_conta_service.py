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


@pytest.fixture
def conta_normal(service):
    return service.cadastrar_conta("1", Decimal("100"))


@pytest.fixture
def conta_bonus(service):
    return service.cadastrar_conta_bonus("2")


@pytest.fixture
def conta_poupanca(service):
    return service.cadastrar_conta_poupanca("3", Decimal("200"))


class TestCadastrarConta:
    def test_cadastrar_conta_normal_com_sucesso(self, service):
        conta = service.cadastrar_conta("1", Decimal("100"))
        assert isinstance(conta, Conta)
        assert conta.numero == "1"
        assert conta.saldo == Decimal("100")

    def test_cadastrar_conta_normal_sem_saldo(self, service):
        with pytest.raises(ValueError, match="deve ser um valor numérico válido"):
            service.cadastrar_conta("2")

    def test_cadastrar_conta_normal_numero_invalido(self, service):
        with pytest.raises(ValueError, match="deve conter apenas dígitos"):
            service.cadastrar_conta("abc", Decimal("100"))

    def test_cadastrar_conta_normal_numero_vazio(self, service):
        with pytest.raises(ValueError, match="deve conter apenas dígitos"):
            service.cadastrar_conta("", Decimal("100"))

    def test_cadastrar_conta_normal_numero_duplicado(self, service):
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
            

class TestCadastrarContaPoupanca:
    def test_cadastrar_conta_poupanca_com_sucesso(self, service):
        conta = service.cadastrar_conta_poupanca("1", Decimal("200"))
        assert isinstance(conta, ContaPoupanca)
        assert conta.numero == "1"
        assert conta.saldo == Decimal("200")

    def test_cadastrar_conta_poupanca_saldo_zero(self, service):
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


class TestBuscarConta:
    def test_buscar_conta_normal(self, service, conta_normal):
        conta = service.buscar_conta("1")
        assert isinstance(conta, Conta)
        assert conta.numero == "1"

    def test_buscar_conta_bonus(self, service, conta_bonus):
        conta = service.buscar_conta("2")
        assert isinstance(conta, ContaBonus)
        assert conta.numero == "2"

    def test_buscar_conta_poupanca(self, service, conta_poupanca):
        conta = service.buscar_conta("3")
        assert isinstance(conta, ContaPoupanca)
        assert conta.numero == "3"

    def test_buscar_conta_inexistente(self, service):
        with pytest.raises(ValueError, match="Não existe conta cadastrada"):
            service.buscar_conta("999")

    def test_buscar_conta_numero_invalido(self, service):
        with pytest.raises(ValueError, match="deve conter apenas dígitos"):
            service.buscar_conta("abc")

    def test_buscar_conta_numero_vazio(self, service):
        with pytest.raises(ValueError, match="deve conter apenas dígitos"):
            service.buscar_conta("")


class TestConsultarSaldo:
    def test_consultar_saldo_normal(self, service, conta_normal):
        saldo = service.consultar_saldo("1")
        assert saldo == Decimal("100")

    def test_consultar_saldo_bonus(self, service, conta_bonus):
        saldo = service.consultar_saldo("2")
        assert saldo == Decimal("0")

    def test_consultar_saldo_poupanca(self, service, conta_poupanca):
        saldo = service.consultar_saldo("3")
        assert saldo == Decimal("200")

    def test_consultar_saldo_inexistente(self, service):
        with pytest.raises(ValueError, match="Não existe conta cadastrada"):
            service.consultar_saldo("999")


class TestCreditar:
    def test_creditar_conta_normal_com_sucesso(self, service, conta_normal):
        saldo = service.creditar("1", "200")
        assert saldo == Decimal("300")

    def test_creditar_conta_poupanca_com_sucesso(self, service, conta_poupanca):
        saldo = service.creditar("3", "50")
        assert saldo == Decimal("250")

    def test_creditar_valor_negativo(self, service, conta_normal):
        with pytest.raises(ValueError, match="deve ser um valor numérico válido"):
            service.creditar("1", "-50")

    def test_creditar_valor_zero(self, service, conta_normal):
        with pytest.raises(ValueError, match="deve ser um valor numérico válido"):
            service.creditar("1", "0")

    def test_creditar_valor_invalido(self, service, conta_normal):
        with pytest.raises(ValueError, match="deve ser um valor numérico"):
            service.creditar("1", "abc")

    def test_creditar_conta_inexistente(self, service):
        with pytest.raises(ValueError, match="Não existe conta cadastrada"):
            service.creditar("999", "100")

    def test_creditar_bonus_pontuacao_aumenta(self, service, conta_bonus):
        service.creditar("2", "300")
        conta = service.buscar_conta("2")
        assert conta.pontuacao == 12


class TestDebitar:
    def test_debitar_conta_normal_com_sucesso(self, service, conta_normal):
        saldo = service.debitar("1", "30")
        assert saldo == Decimal("70")

    def test_debitar_conta_poupanca_com_sucesso(self, service, conta_poupanca):
        saldo = service.debitar("3", "50")
        assert saldo == Decimal("150")

    def test_debitar_valor_negativo(self, service, conta_normal):
        with pytest.raises(ValueError, match="deve ser um valor numérico válido"):
            service.debitar("1", "-50")

    def test_debitar_valor_zero(self, service, conta_normal):
        with pytest.raises(ValueError, match="deve ser um valor numérico válido"):
            service.debitar("1", "0")

    def test_debitar_valor_invalido(self, service, conta_normal):
        with pytest.raises(ValueError, match="deve ser um valor numérico"):
            service.debitar("1", "abc")

    def test_debitar_conta_inexistente(self, service):
        with pytest.raises(ValueError, match="Não existe conta cadastrada"):
            service.debitar("999", "100")

    def test_debitar_saldo_insuficiente(self, service, conta_normal):
        with pytest.raises(ValueError, match="Saldo insuficiente"):
            service.debitar("1", "200")


