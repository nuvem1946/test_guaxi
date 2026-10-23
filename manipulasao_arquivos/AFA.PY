while True:
    print("\n========================")
    print("   GESTÃO ACADÊMICA     ")
    print("========================")
    print("1 - Cadastrar Aluno")
    print("2 - Listar Alunos")
    print("3 - Consultar Aluno")
    print("4 - Alterar Aluno")
    print("5 - Excluir Aluno")
    print("0 - Sair")
    opcao = input("Escolha: ").strip()
    
    match opcao:
        case "1":
            cadastrar_aluno()
        case "2":
            listar_alunos()
        case "3":
            consultar_aluno()
        case "4":
            alterar_aluno()
        case "5":
            excluir_aluno()
        case "0":
            print("Sistema encerrado.")
            break
        case _:
            print("Opção inválida.")

# --- DEFINIÇÃO DAS FUNÇÕES ---
def cadastrar_aluno():
    matricula = input("Matrícula: ")
    nome = input("Nome do Aluno: ")
    curso = input("Curso: ")
    with open("alunos.txt", "a") as arquivo:
        arquivo.write(f"{matricula};{nome};{curso}\n")
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    try:
        with open("alunos.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum aluno cadastrado.")
            return
        print("\n===== LISTA DE ALUNOS =====")
        for posicao, linha in enumerate(linhas, start=1):
            matricula, nome, curso = linha.strip().split(";")
            print(f"{posicao} - Matrícula: {matricula} | Nome: {nome} | Curso: {curso}")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")

def consultar_aluno():
    busca = input("Digite a matrícula para busca: ")
    encontrado = False
    try:
        with open("alunos.txt", "r") as arquivo:
            for linha in arquivo:
                matricula, nome, curso = linha.strip().split(";")
                if matricula == busca:
                    print(f"\nMatrícula: {matricula} | Nome: {nome} | Curso: {curso}")
                    encontrado = True
        if not encontrado:
            print("Aluno não encontrado.")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")

def alterar_aluno():
    try:
        with open("alunos.txt", "w") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum aluno cadastrado.")
            return
        listar_alunos()
        posicao = int(input("\nQual registro deseja alterar? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição inválida.")
            return
        matricula = input("Nova matrícula: ")
        nome = input("Novo nome: ")
        curso = input("Novo curso: ")
        linhas[posicao - 1] = f"{matricula};{nome};{curso}\n"
        with open("alunos.txt", "r") as arquivo:
            arquivo.writelines(linhas)
        print("Registro alterado com sucesso!")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")
    except ValueError:
        print("Digite apenas números.")

def excluir_aluno():
    try:
            with open("alunos.txt", "r") as arquivo:
                linhas = arquivo.readlines()
            if len(linhas) == 0:
                print("Nenhum livro cadastrado.")
                return
            cadastrar_aluno()
            posicao = int(input("\nQual registro deseja excluir? "))
            if posicao < 1 or posicao > len(linhas):
                print("Posição inválida.")
                return
            del linhas[posicao-1]
            with open("alunos.txt", "w") as arquivo:
                arquivo.writelines(linhas)
            print("Registro excluído com sucesso!")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")
    except ValueError:
        print("Digite apenas números.")
    