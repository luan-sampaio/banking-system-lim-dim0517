import os

from repositories.conta_repository import ContaRepository
from services.conta_service import ContaService
from services.conta_poupanca_service import ContaPoupancaService
from controller.conta_controller import ContaController


repository = ContaRepository()
service = ContaService(repository)
conta_poupanca_service = ContaPoupancaService(repository)
controller = ContaController(service, conta_poupanca_service)


def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("========== Banking System L.I.M. ==========\n")
        print("         [1] Cadastrar uma conta")
        print("         [2] Consultar Saldo")
        print("         [3] Adicionar Crédito")
        print("         [4] Realizar Débito")
        print("         [5] Realizar Transferência")
        print("         [6] Render Juros")
        print("         [7] Consultar dados")
        print("         [8] Sair")
        
        opcao = input("\n         Escolha uma opção: ") 
        
        if opcao == "1":
            opcao_conta = tela_contas()

            if opcao_conta == "A":
                print(controller.cadastrar_conta())
            elif opcao_conta == "B":
                print(controller.cadastrar_conta_bonus())
            elif opcao_conta == "C":
                print(controller.cadastrar_conta_poupanca())
            else:
                print("\n         Opção Inválida!")
        elif opcao == "2":
            print(controller.consultar_saldo())
        elif opcao == "3":
            print(controller.creditar())
        elif opcao == "4":
            print(controller.debitar())
        elif opcao == "5":
            print(controller.transferir())
        elif opcao == "6":
            print(controller.render_juros())
        elif opcao == "7":
            print(controller.consultar_dados())
        elif opcao == "8":
            break
        else:
            print("\n         Opção Inválida!")
            
        input("\n     [Pressione Enter para Retornar ao menu]")

def tela_contas():
    os.system("cls" if os.name == "nt" else "clear")
    print("========== Banking System L.I.M. ==========\n")
    print("         Escolha o tipo de conta: \n")
    print("         [A] Conta Normal")
    print("         [B] Conta Bônus")
    print("         [C] Conta Poupança")
    

    return input("\n         Escolha uma opção: ").upper()

main()
