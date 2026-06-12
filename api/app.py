from decimal import Decimal

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

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

class CreditoRequest(BaseModel):
    valor: str


@app.post("/banco/contas/")
def criar_conta(body: CriarContaRequest):
    saldo = body.saldo_inicial.replace(",", ".")
    if body.tipo == "bonus":
        try:
            conta = conta_service.cadastrar_conta_bonus(body.numero)    
        except ValueError as erro:
            raise HTTPException(status_code=400, detail=str(erro))
    elif body.tipo == "poupanca":
        try:
            conta = conta_service.cadastrar_conta_poupanca(body.numero, saldo)
        except ValueError as erro:
            raise HTTPException(status_code=400, detail=str(erro))
    else:
        try:
            conta = conta_service.cadastrar_conta(body.numero, saldo)
        except ValueError as erro:
            raise HTTPException(status_code=400, detail=str(erro))
    return {"numero": conta.numero, "saldo": float(conta.saldo), "mensagem": "Conta cadastrada com sucesso"}

@app.get("/banco/conta/{id}")
def consultar_conta(id: str):
    try:
        dados_conta = conta_service.consultar_dados(id)
        return dados_conta
    except ValueError as erro:
        raise HTTPException(status_code=404, detail=str(erro))

@app.get("/banco/conta/{id}/saldo")
def consultar_saldo(id: str):
    try:
        saldo_conta = conta_service.consultar_saldo(id)
        return {"saldo": float(f"{saldo_conta:.2f}")}
    except ValueError as erro:
        raise HTTPException(status_code=404, detail=str(erro))
    
@app.put("/banco/conta/{id}/credito")
def creditar_conta(id: str, body: CreditoRequest):
    try:
        valor_str = body.valor.replace(",", ".")

        saldo_atualizado = conta_service.creditar(id, valor_str)
        
        return {
            "mensagem": "Crédito realizado com sucesso", 
            "saldo": float(f"{saldo_atualizado:.2f}")
        }
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))