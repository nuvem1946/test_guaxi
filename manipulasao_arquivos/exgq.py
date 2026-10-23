def cadastrar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço (R$): "))
    with open("estoque.txt", "a") as arquivo:
        arquivo.write(f"{nome};{quantidade};{preco}\n")
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    try:
        with open("estoque.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum produto cadastrado.")
            return
        print("\n===== ESTOQUE DE PRODUTOS =====")
        for posicao, linha in enumerate(linhas, start=1):
            nome, qtd, preco = linha.strip().split(";")
            print(f"{posicao} - {nome} | Qtd: {qtd} | R$ {preco}")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")

def consultar_produto():
    busca = input("Digite o nome do produto: ")
    encontrado = False
    try:
        with open("estoque.txt", "r") as arquivo:
            for linha in arquivo:
                nome, qtd, preco = linha.strip().split(";")
                if nome == busca:
                    print(f"\nProduto: {nome} | Qtd: {qtd} | R$ {preco}")
                    encontrado = True
        if not encontrado:
            print("Produto não encontrado.")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")

def excluir_produto():
    try:
        with open("estoque.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum produto cadastrado.")
            return
        listar_produtos()
        posicao = int(input("\nQual registro deseja alterar? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição inválida.")
            return
        nome = input("Novo nome: ")
        qtd = int(input("Nova quantidade: "))
        preco = float(input("Novo preço (R$): "))
        linhas[posicao - 1] = f"{nome};{qtd};{preco}"
        with open("estoque.txt", "w") as arquivo:
            arquivo.writelines(linhas)
        print("Registro alterado com sucesso!")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")
    except ValueError:
        print("Digite apenas números válidos.")

def alterar_produto():
    try:
        with open("estoques.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum produto cadastrado.")
            return
        listar_produtos()
        posicao = int(input("\nQual registro deseja excluir? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição inválida.")
            return
        del linhas[posicao - 1]
        with open("estoque.txt", "w") as arquivo:
            arquivo.writelines(linhas)
        print("Registro excluído com sucesso!")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")
    except ValueError:
        print("Digite apenas números válidos.")

while True:
    print("\n========================")
    print("  CONTROLE DE ESTOQUE   ")
    print("========================")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Consultar Produto")
    print("4 - Alterar Produto")
    print("5 - Excluir Produto")
    print("0 - Sair")
    opcao = input("Escolha: ").strip()
    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        consultar_produto()
    elif opcao == "4":
        alterar_produto()
    elif opcao == "5":
        excluir_produto()
    elif opcao == "0":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida.")