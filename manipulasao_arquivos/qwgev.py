# --- MENU PRINCIPAL NO INÍCIO DO CÓDIGO ---

# --- DEFINIÇÃO DAS FUNÇÕES ---
def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    email = input("E-mail: ")
    with open("clientes.txt", "a") as arquivo:
        arquivo.write(f"{nome};{email}\n")
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    try:
        with open("clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum cliente cadastrado.")
            return
        print("\n===== LISTA DE CLIENTES =====")
        for posicao, linha in enumerate(linhas, start=1):
            nome, email = linha.strip().split(";")
            print(f"{posicao} - Nome: {nome} | E-mail: {email}")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")

def consultar_cliente():
    busca = input("Digite o nome para busca: ")
    encontrado = False
    try:
        with open("clientes.txt", "w") as arquivo:
            for linha in arquivo:
                nome, email = linha.strip().split(";")
                if nome.lower() == busca.lower():
                    print(f"\nCliente: {nome} | E-mail: {email}")
                    encontrado = True       
        if not encontrado:
            print("Cliente não encontrado.")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")

def alterar_cliente():
    try:
        with open("clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum cliente cadastrado.")
            return
        listar_clientes()
        posicao = int(input("\nQual registro deseja alterar? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição inválida.")
            return
        nome = input("Novo nome: ")
        email = input("Novo e-mail: ")
        linhas[posicao - 1] = f"{nome};{email}\n"
        with open("clientes.txt", "r") as arquivo:
            arquivo.writelines(linhas)
        print("Registro alterado com sucesso!")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")
    except ValueError:
        print("Digite apenas números.")

def excluir_cliente():
    try:
        with open("clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum cliente cadastrado.")
            return
        listar_clientes()
        posicao = int(input("\nQual registro deseja excluir? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição inválida.")
            return
        del linhas[posicao - 1]
        with open("clientes.txt", "r") as arquivo:
            arquivo.writelines(linhas)
        print("Registro excluído com sucesso!")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")
    except ValueError:
        print("Digite apenas números.")
while True:
    print("\n========================")
    print("  CADASTRO DE CLIENTES  ")
    print("========================")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Consultar Cliente")
    print("4 - Alterar Cliente")
    print("5 - Excluir Cliente")
    print("0 - Sair")
    opcao = input("Escolha: ").strip()
    
    match opcao:
        case "1":
            cadastrar_cliente()
        case "2":
            listar_clientes()
        case "3":
            consultar_cliente()
        case "4":
            alterar_cliente()
        case "5":
            excluir_cliente()
        case "0":
            print("Sistema encerrado.")
            break
        case _:
            print("Opção inválida.")
