from decimal import Decimal

from fastapi import FastAPI
from pydantic import BaseModel

from repositories.conta_repository import ContaRepository
from services.conta_service import ContaService
from services.conta_poupanca_service import ContaPoupancaService

repository = ContaRepository()
conta_service = ContaService(repository)
conta_poupanca_service = ContaPoupancaService(repository)

app = FastAPI(title="Banking System L.I.M.")


class CriarContaRequest(BaseModel):
    numero: str
    saldo_inicial: str = "0"
    tipo: str = "normal"


@app.post("/banco/contas/")
def criar_conta(body: CriarContaRequest):
    saldo = Decimal(body.saldo_inicial.replace(",", "."))
    if body.tipo == "bonus":
        conta = conta_service.cadastrar_conta_bonus(body.numero)
    elif body.tipo == "poupanca":
        conta = conta_service.cadastrar_conta_poupanca(body.numero, saldo)
    else:
        conta = conta_service.cadastrar_conta(body.numero, saldo)
    return {"numero": conta.numero, "saldo": float(conta.saldo), "mensagem": "Conta cadastrada com sucesso"}
