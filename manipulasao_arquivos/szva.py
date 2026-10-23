 --- MENU PRINCIPAL NO INÍCIO DO CÓDIGO ---
while True:
    print("\n========================")
    print("   CLÍNICA MÉDICA - PACIENTES   ")
    print("========================")
    print("1 - Cadastrar Paciente")
    print("2 - Listar Pacientes")
    print("3 - Consultar Paciente")
    print("4 - Alterar Paciente")
    print("5 - Excluir Paciente")
    print("0 - Sair")
    opcao = input("Escolha: ").strip()
    
    match opcao:
        case "1":
            cadastrar_paciente()
        case "2":
            listar_pacientes()
        case "3":
            consultar_paciente()
        case "4":
            alterar_paciente()
        case "5":
            excluir_paciente()
        case "0":
            print("Sistema encerrado.")
            break
        case _:
            print("Opção inválida.")

# --- DEFINIÇÃO DAS FUNÇÕES ---
def cadastrar_paciente():
    cpf = input("CPF: ")
    nome = input("Nome do paciente: ")
    with open("pacientes.txt", "a") as arquivo:
        arquivo.write(f"{cpf};{nome}\n")
    print("Paciente cadastrado com sucesso!")

def listar_pacientes():
    try:
        with open("pacientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum paciente cadastrado.")
            return
        print("\n===== PRONTUÁRIOS DE PACIENTES =====")
        for posicao, linha in enumerate(linhas, start=1):
            cpf, nome = linha.strip().split(";")
            print(f"{posicao} - CPF: {cpf} | Nome: {nome}")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")

# ATENÇÃO: Observe a assinatura e o corpo das duas funções abaixo
def alterar_paciente():
    busca = input("Digite o CPF para busca: ")
    encontrado = False
    try:
        with open("pacientes.txt", "w") as arquivo:
            for linha in arquivo:
                cpf, nome = linha.strip().split(";")
                if cpf == busca:
                    print(f"\nCPF: {cpf} | Nome: {nome}")
                    encontrado = True
        if not encontrado:
            print("Paciente não encontrado.")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")

def consultar_paciente():
    try:
        with open("pacientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum paciente cadastrado.")
            return
        listar_pacientes()
        posicao = int(input("\nQual registro deseja alterar? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição inválida.")
            return
        cpf = input("Novo CPF: ")
        nome = input("Novo nome: ")
        linhas[posicao - 1] = f"{cpf};{nome}\n"
        with open("pacientes.txt", "w") as arquivo:
            arquivo.writelines(linhas)
        print("Registro alterado com sucesso!")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")
    except ValueError:
        print("Digite apenas números.")

def excluir_paciente():
    try:
        with open("pacientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum paciente cadastrado.")
            return
        listar_pacientes()
        posicao = int(input("\nQual registro deseja excluir? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição inválida.")
            return
        del linhas[posicao - 1]
        with open("pacientes.txt", "w") as arquivo:
            arquivo.writelines(linhas)
        print("Registro excluído com sucesso!")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")
    except ValueError:
        print("Digite apenas números.")