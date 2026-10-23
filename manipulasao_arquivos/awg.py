while True:
    print("\n========================")
    print("   GESTÃO DE VEÍCULOS   ")
    print("========================")
    print("1 - Cadastrar Veículo")
    print("2 - Listar Veículos")
    print("3 - Consultar Veículo")
    print("4 - Alterar Veículo")
    print("5 - Excluir Veículo")
    print("0 - Sair")
    opcao = input("Escolha: ").strip()
    
    match opcao:
        case "1":
            cadastrar_veiculo()
        case "2":
            listar_veiculos()
        case "3":
            consultar_veiculo()
        case "4":
            alterar_veiculo()
        case "5":
            excluir_veiculo()
        case "0":
            print("Sistema encerrado.")
            break
        case _:
            print("Opção inválida.")

# --- DEFINIÇÃO DAS FUNÇÕES ---
def cadastrar_veiculo():
    placa = input("Placa: ")
    modelo = input("Modelo: ")
    with open("veiculos.txt", "a") as arquivo:
        arquivo.write(f"{placa};{modelo}\n")
    print("Veículo cadastrado com sucesso!")

def listar_veiculos():
    try:
        with open("veiculos.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum veículo cadastrado.")
            return
        print("\n===== FROTA DE VEÍCULOS =====")
        for posicao, linha in enumerate(linhas, start=1):
            placa, modelo = linha.strip().split(";")
            print(f"{posicao} - Placa: {placa} | Modelo: {modelo}")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")

def consultar_veiculo():
    busca = input("Digite a placa para busca: ")
    encontrado = False
    try:
        with open("veiculos.txt", "r") as arquivo:
            for linha in arquivo:
                placa, modelo = linha.strip().split(";")
                if placa.lower() == busca.lower():
                    print(f"\nPlaca: {placa} | Modelo: {modelo}")
                    encontrado = True
        if not encontrado:
            print("Veículo não encontrado.")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")

def alterar_veiculo():
    try:
        with open("veiculos.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum veículo cadastrado.")
            return
        listar_veiculos()
        posicao = int(input("\nQual registro deseja alterar? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição inválida.")
            return
        placa = input("Nova placa: ")
        modelo = input("Novo modelo: ")
        linhas[posicao-1] = f"{placa};{modelo}\n"
        with open("veiculos.txt", "w") as arquivo:
            arquivo.writelines(linhas)
        print("Registro alterado com sucesso!")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")
    except ValueError:
        print("Digite apenas números.")

def excluir_veiculo():
    try:
        with open("veiculos.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum veículo cadastrado.")
            return
        listar_veiculos()
        posicao = int(input("\nQual registro deseja excluir? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição inválida.")
            return
        del linhas[posicao - 1]
        with open("veiculos.txt", "w") as arquivo:
            arquivo.writelines(linhas)
        print("Registro excluído com sucesso!")
    except FileNotFoundError:
        print("Arquivo ainda não existe.")
    except ValueError:
        print("Digite apenas números.")