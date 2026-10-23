import os

def limapa_tela():
    os.system("cls")

def cadatrar():
    print("cadastrar")

def time():
    print("time")

def consultar():
    print("consultar")

def alterar():
    print("alterar")

def sair():
    print("sair")

def excluir():
    print("excluir")

while True:

    print("==============================")
    print("     CADASTRO DE GUAXIX")
    print("==============================")
    print("1-cadastro do guaxi")
    print("2-time")
    print("3-quantos anos")
    print("4-qual seu sabor favorito")
    print("5-lista dos guaxix cadastrados")
    print("6-deletar um guaxi")
    print("0-sair")

    opc=int(input("escolha: "))

    if opc==1:
        cadatrar()

    elif opc==2:
        time()
    elif opc==3:
        consultar()
    elif opc==4:
        alterar()
    elif opc==5:
        sair()
    elif opc==6:
        excluir()

    elif opc==0:
        print("programa encerado")
        break
    else:
        print("opção invalida")

    input("pressione ENTER para continuar")