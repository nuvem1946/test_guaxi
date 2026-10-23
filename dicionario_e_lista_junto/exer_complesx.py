import os
lightwuz=[]
def limapa_tela():
    os.system("cls")

def cadatrar():
    print("cadastrar")

def consultar_time():
    for _ ,guaxi in enumerate(lightwuz):
        print(f"{_} {lightwuz['nick']} {lightwuz['time']}")


def consultar():
    for _ ,lightwuz in enumerate(lightwuz):
            print(f"{_} {lightwuz['nick']} {lightwuz['ano']}")
def alterar():
     for _ ,lightwuz in enumerate(lightwuz):
            print(f"{_} {lightwuz['nick']} {lightwuz['sabor']}")

def sair():
    print("sair")

def excluir():
    if len(lightwuz)==0:
        print("nenhum guaxi encontrado no bazar")
            
    for indice, guaxi in enumerate(lightwuz):
        print(f"{indice} {guaxi['nick']}")
    Codigo=int(input("digite o numero do guaxi: "))

    if Codigo>= 0 and Codigo<len(lightwuz):
        #lightwuz.pop(Codigo)
        del lightwuz[Codigo]
        print("guaxi excluido")

    else:
        print("codigo invalido")
    
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
        
    opc=int(input("qual opsão deseja: "))
    if opc==1:

        nick=input("qual o seu nickname: ")
        time=input("yumer ou lighterrr: ")
        ano=input("quantos anos: ")
        sabor=input("qual o seu sabor favorito: ")
        yumer={
            "nick":nick,
            "time":time,
            "ano":ano,
            "sabor":sabor
        }
        lightwuz.append(yumer)
        print("guaxi armazenado")
      
    elif opc==2:
        consultar_time()
    elif opc==3:
       consultar()

    elif opc==4:
       alterar()

    elif opc==5:
        print(lightwuz)

    elif opc==6:
        excluir()
        

    elif opc==0:
        print("saindo da gerasão de guaxis")
        break