def cadastrar_entrega():
    destino=input("qual o seu destino: ")
    peso=float(input("peso (kg): "))

    with open("entregas.txt","a") as arquivos:
        arquivos.write(f"{destino};{peso}")
    print("entrega cadastrada com susseco! ")

def listar_entregas():
    try:
        with open("entregas.txt","r") as arquivos:
            linhas= arquivos.readline()
        if len(linhas)==0:
            print("nenhuma entrega cadastrada.")
            return
        print("===== LISTA DE ENTREGA =====")
        for posicao,linha in enumerate (linhas,start=1):
            destino,peso=linha.strip().split(";")
            print(f"{posicao}-{destino}| {peso } KG")             
    except FileExistsError:
            print("arquivo não encontrado | ┬┬﹏┬┬ |")        
    input("\n precione qualquer tecla para voltar ao menu....")
    return

def consulta_entrega():
    busca=input("digite o destino: ")
    encontrado=False
    try:
        with open("entregas.txt","r") as arquivos:
            for linhas in arquivos:
                  destino,peso=linhas.trip().split(";")
                  if destino.lower()==busca.lower():
                    print(f" desnitino: {destino}| peso {peso} KG")
        if not encontrado:
            print("destino não encontrado. ") 
    except FileExistsError:
                print("arquivo não encontrado | ┬┬﹏┬┬ |")        
    input("\n precione qualquer tecla para voltar ao menu....")
    return

def alterar_entrega():
    try:
        with open("entrega.txt","r") as arquivos:
            linhas= arquivos.readline()
        if len(linhas)==0:
            print("nenhuma entrega encontrada. ")
            return
        listar_entregas()
        posicao=int(input("qaul registro deseja alterar? "))
        if posicao<1 or posicao> len(linhas):
            print("posição invalida.")
            return
        destino=input("novo destino: ")
        peso=float(input("novo pesso: "))
        linhas[posicao-1]=f"{destino};{peso}"
    except FileExistsError:
                    print("arquivo não encontrado | ┬┬﹏┬┬ |")      
    except ValueError:
         print("digite apenas um numero ")  
    input("\n precione qualquer tecla para voltar ao menu....")
    return

def excluir_entrega():
    try:
        with open("entregar.txt","r") as arquivos:
            linhas=arquivos.readline()
        if  len(linhas)==0:
            print("nenhuma entrega cadastrada. . ")
            return
        listar_entregas()
        posicao=int(input("qual registro deseja excluir: "))
        if posicao<1 or posicao> len (linhas):
            print("posição invalida.")
    except FileExistsError:
                        print("arquivo não encontrado | ┬┬﹏┬┬ |")      
    except ValueError:
             print("digite apenas um numero ")  
    input("\n precione qualquer tecla para voltar ao menu....")
    return
while True:
    print("\n========================")
    print(" PAINEL DE TRANSPORTES ")
    print("========================")
    print("1 - Cadastrar Entrega")
    print("2 - Listar Entregas")
    print("3 - Consultar Entrega")
    print("4 - Alterar Entrega")
    print("5 - Excluir Entrega")
    print("0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "1":
        cadastrar_entrega()
    elif opcao == "2":
        listar_entregas()
    elif opcao == "3":
        consulta_entrega()
    elif opcao == "4":
        alterar_entrega()
    elif opcao == "5":
        excluir_entrega()
    elif opcao == "0":
        print("Sistema encerrado.")
        break
    else:
        print("Opcao invalida.")