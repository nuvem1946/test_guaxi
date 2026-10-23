
def cadastrar():
    while True:
        print("=======-----CADASTRO-----========")
        senha_clie=input("qual sua senha: ")
        nome_clie=input("qual seu nome: ")
        with open("cliente.txt","a")as arquivo:
                arquivo.write(f"{nome_clie};{senha_clie}\n")
                
        print ("Cadastro realizado!")
        continuar = input ("Deseja cadastrar outra cliente? (s/n): ")
        if continuar.lower() !="s":
            print ("Desligando...")
            break
def listar():
    print("=======-------LISTA------=======")
    try:
        with open("cliente.txt","r") as arquivo:
                linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhuma cliente cadastrada")
            return
        for posicao, linha in enumerate(linhas,start=1):
            nome_clie,senha_clie = linha.strip().split(";") #strip = remove, move  split = adiciona algo
            print(posicao,"-",nome_clie,"-",senha_clie)
    except FileNotFoundError:
            print("Nenhuma roupa cadastrada.")
def consultar():
    print("========--------CONSULTAR------========")
    busca = input("Digite o cliente: ")
    encontrada = False
    try:
        with open("cliente.txt","r") as arquivo:
            for linha in arquivo:
                nome_clie,senha_clie = linha.strip().split(";")
                if nome_clie.lower() == busca.lower():
                    print ("NOME ",nome_clie)
                    print ("SENHA ",senha_clie)
                    encontrada = True
            if not encontrada:
                print("Cliente não encontrado!")
    except FileNotFoundError:
            print("Nenhuma roupa encontrada!")
            return
def alterar():
    print("======-----ALTERAR-----=======")
    try:
            with open("cliente.txt","r") as arquivo:
                linhas = arquivo.readlines()
            if len(linhas) == 0:
                print ("Nenhuma roupa cadastrada!@#!")
                return
            listar()
            posicao = int(input("Qual cliente deseja alterar? \n"))
            if posicao < 1 or posicao > len(linhas):
                print("Posição Inválida!")
                return
            nova_nome_clie = input("Novo nome: ")
            novo_senha_clie = input ("Novo senha: ")
            linhas[posicao-1]=f"{nova_nome_clie};{novo_senha_clie}\n"
            with open("cliente.txt","w") as arquivo:
                arquivo.writelines(linhas)
                print("Roupa alterada com sucesso!")
    except FileNotFoundError:
        print ("Nada encontrado")
    except ValueError:
        print ("Digite um número existente na lista")
def morra():
    print("========------EXCLUIR-----========")    
    try:
            with open("cliente.txt","r") as arquivo:
                linhas = arquivo.readlines()
            if len(linhas) == 0:
                print ("Nenhuma cliente cadastrada!@#!")
                return
            posicao = int(input("Qual cliente deseja excluir? "))
            if posicao < 1 or posicao > len(linhas):
                print("Posição Inválida!")
                return
            del linhas[posicao-1]
            with open("cliente.txt","w") as arquivo:
                linhas = arquivo.writelines(linhas)
            print ("Roupa excluída com sucesso!")
    except FileNotFoundError:
            print("Arquivo não encontrado!!")
    except ValueError:
            print("Dgigite um valor a lista")

def cadastrar_for():
    while True:
        print("=======-----CADASTRO-----========")
        senha_clie=input("qual sua senha: ")
        nome_clie=input("qual seu nome: ")
        with open("fornecedor.txt","a")as arquivo:
                arquivo.write(f"{nome_clie};{senha_clie}\n")
                
        print ("Cadastro realizado!")
        continuar = input ("Deseja cadastrar outra roupa? (s/n): ")
        if continuar.lower() !="s":
            print ("Desligando...")
            break
def listar_for():
    print("=======-------LISTA------=======")
    try:
        with open("fornecedor.txt","r") as arquivo:
                linhas = arquivo.readlines()
        if len(linhas) == 0:
                    print("Nenhuma roupa cadastrada")
                    return
        for posicao, linha in enumerate(linhas,start=1):
            nome_clie,senha_clie = linha.strip().split(";") #strip = remove, move  split = adiciona algo
            print(posicao,"-",nome_clie,"-",senha_clie)
    except FileNotFoundError:
        print("Nenhuma roupa cadastrada.")
def consultar_for():
    print("========--------CONSULTAR------========")
    busca = input("Digite a marca: ")
    encontrada = False
    try:
        with open("fornecedor.txt","r") as arquivo:
            for linha in arquivo:
                nome_clie,senha_clie = linha.strip().split(";")
                if nome_clie.lower() == busca.lower():
                    print ("NOME ",nome_clie)
                    print ("SENHA ",senha_clie)
                    encontrada = True
            if not encontrada:
                print("Cliente não encontrado!")       
    except FileNotFoundError:
            print("Nenhuma roupa encontrada!")
            return
def alterar_for():
    print("======-----ALTERAR-----=======")
    try:
            with open("fornecedor.txt","r") as arquivo:
                linhas = arquivo.readlines()
            if len(linhas) == 0:
                print ("Nenhuma roupa cadastrada!@#!")
                return
            posicao = int(input("Qual roupa deseja alterar? "))
            if posicao < 1 or posicao > len(linhas):
                print("Posição Inválida!")
                return
            nova_nome_clie = input("Novo nome: ")
            novo_senha_clie = input ("Novo senha: ")
            linhas[posicao-1]=f"{nova_nome_clie};{novo_senha_clie}\n"
            with open("fornecedor.txt","w") as arquivo:
                arquivo.writelines(linhas)
                print("Roupa alterada com sucesso!")
    except FileNotFoundError:
        print ("Nada encontrado")
    except ValueError:
        print ("Digite um número existente na lista")
def morra_for():
    print("========------EXCLUIR-----========")    
    try:
            with open("fornecedor.txt","r") as arquivo:
                linhas = arquivo.readlines()
            if len(linhas) == 0:
                print ("Nenhuma roupa cadastrada!@#!")
                return
            posicao = int(input("Qual roupa deseja excluir? "))
            if posicao < 1 or posicao > len(linhas):
                print("Posição Inválida!")
                return
            del linhas[posicao-1]
            with open("fornecedor.txt","w") as arquivo:
                linhas = arquivo.writelines(linhas)
            print ("Roupa excluída com sucesso!")
    except FileNotFoundError:
            print("Arquivo não encontrado!!")
    except ValueError:
            print("Dgigite um valor a lista")

def menu_cliente():
        while True:

            print("==============================")
            print("          CLIENTE ")
            print("==============================")
            print("1-cadastrar")
            print("2-lista")
            print("3-consultar")
            print("4-alterar")
            print("5-excluir")
            print("0-sair")
            print("===============================")

            escolha = int(input("Sua escolha: "))
            if escolha == 1:
                cadastrar()
            elif escolha == 2:
                listar()
            elif escolha == 3:
                consultar()
            elif escolha == 4:
                alterar()
            elif escolha==5:
                morra()
            elif escolha==0:
                 break
def menu_fornecedor():
    while True:
    
                print("==============================")
                print("          FORNECEDOR ")
                print("==============================")
                print("1-cadastrar")
                print("2-lista")
                print("3-consultar")
                print("4-alterar")
                print("5-excluir")
                print("6-ver fornecedor")
                print("0-sair")
                print("===============================")
    
                escolha = int(input("Sua escolha: "))
                if escolha == 1:
                    cadastrar_for()
                elif escolha == 2:
                    listar_for()
                elif escolha == 3:
                    consultar_for()
                elif escolha == 4:
                    alterar_for()
                elif escolha==5:
                    morra_for()
while True:
    print("===================================")
    print("          MENU PRINCIPAL")
    print("1-MENU DO CLIENTE")
    print("2-MENU DO FORNECEDOR")
    print("3-SAIR")

    opc_prin=int(input("qual opsão deseja: "))

    if opc_prin==1:
        menu_cliente()
    elif opc_prin==2:
        menu_fornecedor()
    else:
         print("sair")