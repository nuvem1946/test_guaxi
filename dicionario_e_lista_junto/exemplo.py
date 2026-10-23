def cadastrar():
    while True:
        print ("\n ===== CADASTRO DE ROUPAS =====")
        marca = input("Digite a marca: ")
        tamanho = input("Digite o tamanho: ")
        with open("roupas.txt","a")as arquivo:
            arquivo.write(f"{marca};{tamanho}\n")

        print ("Cadastro realizado!")
        continuar = input ("Deseja cadastrar outra roupa? (s/n): ")
        if continuar.lower() !="s":
            print ("Desligando...")
            break

def listar():
    print("\n ====== LISTAR ROUPA ======")
    try:
        with open("roupas.txt","r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhuma roupa cadastrada")
            return
        for posicao, linha in enumerate(linhas,start=1):
            marca, tamanho = linha.strip().split(";") #strip = remove, move  split = adiciona algo
            print(posicao,"-",marca,"-",tamanho)
    except FileNotFoundError:
        print("Nenhuma roupa cadastrada.")

def consultar():
    print("\n ====== CONSULTAR ROUPA ======")
    busca = input("Digite a marca: ")
    encontrada = False
    try:
        with open("roupas.txt","r") as arquivo:
            for linha in arquivo:
                marca,tamanho = linha.strip().split(";")
                if marca.lower() == busca.lower():
                    print ("Marca: ",marca)
                    print ("Tamanho: ", tamanho)
                    encontrada = True
    except FileNotFoundError:
        print("Nenhuma roupa encontrada!")
        return
    if encontrada == False:
        print ("Roupa não encontrada.")

def alterar():
    print("\n ====== Alterar Roupa ======")
    try:
        with open("roupas.txt","r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print ("Nenhuma roupa cadastrada!@#!")
            return
        posicao = int(input("Qual roupa deseja alterar? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição Inválida!")
            return
        nova_marca = input("Nova marca: ")
        novo_tamanho = input ("Novo tamanho: ")
        linhas[posicao-1]=f"{nova_marca};{novo_tamanho}\nm"
        with open("roupas.txt","w") as arquivo:
            arquivo.writelines(linhas)
            print("Roupa alterada com sucesso!")
    except FileNotFoundError:
        print ("Nada encontrado")
    except ValueError:
        print ("Digite um número existente na lista")

def excluir():
    print("\n ====== Excluir Roupa ======")
    try:
        with open("roupas.txt","r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print ("Nenhuma roupa cadastrada!@#!")
            return
        posicao = int(input("Qual roupa deseja excluir? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição Inválida!")
            return
        del linhas[posicao-1]
        with open("roupas.txt","w") as arquivo:
            linhas = arquivo.writelines(linhas)
        print ("Roupa excluída com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado!!")
    except ValueError:
        print("Dgigite um valor a lista")
        
while True:
    print (" = / = / = / = Cadastro de Roupas = / = / = / =")
    print ("Por favor, escolha uma das opções a seguie:")
    print ("1 - Cadastrar uma roupa")
    print ("2 - Listar roupas cadastradas")
    print ("3 - Consultar roupas")
    print ("4 - Alterar roupa")
    print ("5 - Sair")
    escolha = int(input("Sua escolha: "))
    if escolha == 1:
        cadastrar()
    elif escolha == 2:
        listar()
    elif escolha == 3:
        consultar()
    elif escolha == 4:
        alterar()
    elif escolha == 5:
        ("Desligando sistema...")
        break
    else:
        ("Erro.Tente novamente")