import os

from repositories.conta_repository import ContaRepository
from services.conta_service import ContaService
from controller.conta_controller import ContaController


repository = ContaRepository()
service = ContaService(repository)
controller = ContaController(service)


def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("========== Banking Sytem L.I.M. ==========\n")
        print("         [1] Cadastrar uma conta")
        print("         [2] Consultar Saldo")
        print("         [3] Adicionar Crédito")
        print("         [4] Realizar Débito")
        print("         [5] Realizar Transferência")
        print("         [6] Sair")
        
        opcao = input("\n         Escolha uma opção: ") 
        
        if opcao == "1"       :
            print(controller.cadastrar_conta())
        elif opcao == "6":
            break
        else:
            print("\n         Opção Inválida!")
            
        input("\n     [Pressione Enter para Retornar ao menu]")

main()
