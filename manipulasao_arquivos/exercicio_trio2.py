def cadastrar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    with open("biblioteca.txt", "a") as arquivo:
        arquivo.write(f"{titulo};{autor}\n")
    print("Livro cadastrado com sucesso!")

def listar_livros():
    try:
        with open("biblioteca.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum livro cadastrado.")
            return
        print("\n===== LISTA DE LIVROS =====")
        for posicao, linha in enumerate(linhas, start=1):
            titulo, autor = linha.strip().split(";")
            print(f"{posicao} - {titulo} | Autor: {autor}")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")

def consultar_livro():
    busca = input("Digite o título para busca: ")
    encontrado = False
    try:
        with open("biblioteca.txt", "r") as arquivo:
            for linha in arquivo:
                titulo, autor = linha.strip().split(";")
                if titulo.lower() == busca.lower():
                    print(f"\nLivro encontrado: {titulo} | Autor: {autor}")
                    encontrado = True
        if not encontrado:
            print("Livro não encontrado.")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")

def alterar_livro():
    try:
        with open("biblioteca.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum livro cadastrado.")
            return
        listar_livros()
        posicao = int(input("\nQual registro deseja alterar? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição inválida.")
            return
        titulo = input("Novo título: ")
        autor = input("Novo autor: ")
        linhas[posicao - 1] = f"{titulo};{autor}\n"
        with open("biblioteca.txt", "w") as arquivo:
            arquivo.writelines(linhas)
        print("Registro alterado com sucesso!")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")
    except ValueError:
        print("Digite apenas números.")

def excluir_livro():
    try:
        with open("biblioteca.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum livro cadastrado.")
            return
        listar_livros()
        posicao = int(input("\nQual registro deseja excluir? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição inválida.")
            return
        del linhas[posicao-1]
        with open("biblioteca.txt", "w") as arquivo:
            arquivo.writelines(linhas)
        print("Registro excluído com sucesso!")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")
    except ValueError:
        print("Digite apenas números.")

while True:
    print("\n========================")
    print(" CONTROLE DE BIBLIOTECA ")
    print("========================")
    print("1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Consultar Livro")
    print("4 - Alterar Livro")
    print("5 - Excluir Livro")
    print("0 - Sair")
    opcao = input("Escolha: ")
    match opcao:
        case "1":
            cadastrar_livro()
        case "2":
            listar_livros()
        case "3":
            consultar_livro()
        case "4":
            alterar_livro()
        case "5":
            excluir_livro()
        case "0":
            print("Sistema encerrado.")
            break
        case _:
            print("Opção inválida.")