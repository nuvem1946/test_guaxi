def cadastrar_entrega():
    destino = input("Destino: ")
    peso = float(input("Peso (Kg): "))
    with open("entregas.txt", "a") as arquivo:
        arquivo.write(f"{destino};{peso}\n")
    print("Entrega cadastrada com sucesso!")

def listar_entregas():
    try:
        with open("entregas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhuma entrega cadastrada.")
            return
        print("\n===== LISTA DE ENTREGAS ======")
        for posicao, linha in enumerate(linhas, start=1): 
            destino, peso = linha.strip().split(";")
            print(f"{posicao} - {destino} | {peso} kg")
    except FileNotFoundError:
        print("Arquivo não encontrado")

def consultar_entrega():
    listar_entregas()
    busca = input("Digite o destino: ")
    encontrado = False
    try:
        
        with open("entregas.txt","r") as arquivo:
            for linha in arquivo:
                destino, peso = linha.strip().split(";")
                if destino.lower() == busca.lower():
                    print(f"\nDestino: {destino} | Peso: {peso} kg")
                    encontrado = True
        if not encontrado:
            print("Destino não encontrado.")
    except FileNotFoundError:
        print("Arquivo ainda não existe")

def alterar_entrega():
    try:
        with open("entregas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhuma entrega cadastrada.")
            return
        listar_entregas()
        posicao = int(input("\nQual registro deseja alterar? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição inválida.")
            return
        destino = input("Novo destino: ")
        peso = float(input("Novo peso (kg): "))
        linhas[posicao - 1] = f"{destino};{peso}\n"
        with open("entregas.txt", "w") as arquivo:
            arquivo.writelines(linhas)
        print("Registro alterado com sucesso!")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")
    except ValueError:
        print("Digite apenas números.")

def excluir_entrega():
    try:
        with open("entregas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhuma entrega cadastrada.")
            return
        listar_entregas()
        posicao = int(input("\nQual registro deseja excluir? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição inválida.")
            return
        del linhas[posicao - 1]
        with open("entregas.txt", "w") as arquivo:
            arquivo.writelines(linhas)
        print("Registro excluído com sucesso!")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")
    except ValueError:
        print("Digite apenas números.")

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
        consultar_entrega()
    elif opcao == "4":
        alterar_entrega()
    elif opcao == "5":
        excluir_entrega()
    elif opcao == "0":
        print("Sistema encerrado.")
        break
    else:
        print("Opcao invalida.")