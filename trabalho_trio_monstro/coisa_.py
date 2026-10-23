import time
import os



'''                            CADASTRO DE USUARIOS E LOJAS                              '''


def cadastros():
    
    while True:
        os.system("cls")
        print("======== 🎮 CADASTROS 🎮 ========")
        print("Você vai se cadastrar como usuario ou como loja?")
        print("Digite (U) para usuario ou digite (L) para loja ou (E) para entrar cadastrado")
        escolha = input("Escolha: ")

        if escolha.upper() == "U":
            os.system("cls")
            nickname = input("Insira nome de usuario: ")
            email = input("Insira email: ")
            senha = input("Insira senha: ")
            with open("usuarios.txt", "a")as arquivo:
                arquivo.write(f"{nickname}|{email}|{senha}\n")
                print("Cadastrando...")
                time.sleep(2)
                print("Usuario cadastrado ✅")
                time.sleep(3)
                cadastros()
                

        

        elif escolha.upper() == "L":
            os.system("cls")
            nome_loja = input("Insira nome da loja: ")
            jogo_principal = input("Insira jogo principal: ")
            itens_aceitos = ["moedas","itens","contas"]
            while True:
                tipo_item = input("Insira tipo de venda (moedas/itens/contas): ")
                if tipo_item in itens_aceitos:
                    with open("lojas.txt", "a")as arquivo:
                        arquivo.write(f"{nome_loja}|{jogo_principal}|{tipo_item}\n")
                        print("Cadastrando...")
                        time.sleep(2)
                        print("Loja cadastrada ✅")
                        time.sleep(3)
                        cadastros()
                else:
                    print("Cadastrando...")
                    time.sleep(2)
                    print("Opção de venda inválida ❌")
                    print("Digite um tipo válido")
                    time.sleep(3)

        elif escolha.upper() == "E":
            print("Deseja navegar como (U) usuario ou como (L) loja:")
            selecione = input("Escolha")

            if selecione.upper() == "U":
                menu_usuario()
            elif selecione.upper() == "L":
                menu_lojas()

                

'''============================================================================================================='''

'''                            SUB MENU DE USUARIOS LOGADOS                              '''

'''============================================================================================================='''

def listar_lojas_usuario():
    print("===== LISTA LOJAS =====")
    try:
        with open("lojas.txt","r") as arquivo:
            linhas=arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhuma loja no sistema.")
        for posicao,linha in enumerate(linhas,start=1):
            nome_loja,jogo_principal,tipo_item=linha.strip().split("|")
            print(posicao,"-",nome_loja,"-",jogo_principal,"-",tipo_item)
    except FileNotFoundError:
        print("Arquivo inexistente.")


def consultar_lojas_usuario():
    print("\n===== CONSULTAR LOJAS =====")
    busca=input("Digite o nome da loja: ")
    encontrada=False
    try:
        with open("lojas.txt","r") as arquivo:
            for linha in arquivo:
                nome_loja,jogo_principal,tipo_item=linha.strip().split("|")
                if nome_loja.lower()==busca.lower():
                    print("Nome da loja:",nome_loja)
                    print("Jogo principal:",jogo_principal)
                    print("Item:",tipo_item)
                    encontrada=True
    except FileNotFoundError:
        print("Local não encontrado!")
        return
    if encontrada==False:
        print("Loja não encontrada.")
        


def comprar():
    print("===== LISTA LOJAS =====")
    try:
        with open("lojas.txt","r") as arquivo:
            linhas=arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhuma loja no sistema.")
        for posicao,linha in enumerate(linhas,start=1):
            nome_loja,jogo_principal,tipo_item=linha.strip().split("|")
            print(nome_loja,"-",jogo_principal,"-",tipo_item)
    except FileNotFoundError:
        print("Arquivo inexistente.")            
    while True:
        consultar_lojas_usuario()

        opcao = input("Deseja comprar item cadastrado a loja (S/N): ")

        if opcao.upper() == "S":
            print("Comprado!")
            break

        else:
            print("Retornando")


def menu_usuario():
    while True:
        print("===== MENU USUARIO =====")
        print("1)Listar lojas\n2)Consultar lojas\n3)Comprar\n4)Configurações\n5)Sair")
        chose = input("Escolha: ")
        match chose:
            case "1":
                listar_lojas_usuario()
            case "2":
                consultar_lojas_usuario()
            case "3":
                comprar()
            case "4":
                configs_usuario()
            case "5":
                cadastros()


'''============================================================================================================='''

'''                            SUB-SUB MENU DE USUARIOS LOGADOS                              '''

'''============================================================================================================='''


def listar_usuarios():
    try:
        with open("usuarios.txt","r") as arquivo:
            linhas=arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhuma usuario no sistema.")
        for posicao,linha in enumerate(linhas,start=1):
            nickname,email,senha=linha.strip().split("|")
            print(posicao,"-",nickname,"-",email,"-",senha)

    except FileNotFoundError:
        print("Arquivo inexistente.")


def consultar_usuarios():
    print("===== CONSULTAR USUARIOS =====")
    busca=input("Digite o nickname: ")
    encontrada=False
    try:
        with open("usuarios.txt","r") as arquivo:
            for linha in arquivo:
                nickname,email,senha=linha.strip().split("|")
                if nickname.lower()==busca.lower():
                    print(f"Nickname:{nickname}")
                    print(f"Email:{email}")
                    print(f"Senha:{senha}")
                    encontrada=True
    except FileNotFoundError:
        print("Local não encontrado!")
        return
    if encontrada==False:
        print("Não achou.")    


def alterar_usuario():
    try:
        with open("usuarios.txt","w") as arquivos:
               linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhum produto cadastrado.")
            return
        posicao = int(input("\nQual registro deseja alterar? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição inválida.")
            return
        nickname = input("Novo nome: ")
        senha = int(input("Novo email: "))
        email = float(input("Nova senha: "))
        linhas[posicao - 1] = f"{nickname};{email};{senha}"
        with open("usuarios.txt", "w") as arquivo:
            arquivo.writelines(linhas)
            print("Registro alterado com sucesso!")

    except FileExistsError:
        print("")
    
def excluir_usuario():
    print("\n====== EXCLUIR USUARIOS ======")
    try:
        with open("usuarios.txt","r") as arquivo:
            linhas=arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhuma usuario cadastrado no sistema.")
            return
        #listar()
        posicao=int(input("Qual usuario deseja excluir: "))       
        if posicao <1 or posicao > len(linhas):
            print("Posição invalida.")
            return
        del linhas[posicao-1]
        with open("usuarios.txt","w") as arquivo:
            linhas=arquivo.writelines(linhas)
        print("Usuario excluido com sucesso!")
    except FileNotFoundError:
        print("Arquivo nãoe contrado!")
    except ValueError:
        print("Digite um valor valido na lista")


def configs_usuario():
    while True:
        print("====== MENU USUARIO CONFIGS ======")
        print("1)Listar usuarios\n2)Consultar usuarios\n3)Excluir\n4)Sair")
        ops_loja=int(input("Qual opção deseja: "))
        
        if ops_loja=="1":
            listar_usuarios()
        elif ops_loja=="2":
            consultar_usuarios()
        elif ops_loja=="3":
            excluir_usuario()
        elif ops_loja=="4":
            break

'''============================================================================================================='''

'''                            SUB-SUB MENU DE LOJAS LOGADAS                              '''

'''============================================================================================================='''
def listar_lojas():
    try:
        with open("lojas.txt","r") as arquivo:
            linhas=arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhuma usuario no sistema.")
        for posicao,linha in enumerate(linhas,start=1):
            nome_loja,jogo_principal,tipo_item=linha.strip().split("|")
            print(posicao,"-",nome_loja,"-",jogo_principal,"-",tipo_item)

    except FileNotFoundError:
        print("Arquivo inexistente.")


def consultar_lojas():
    print("===== CONSULTAR LOJAS =====")
    busca=input("Digite o nickname: ")
    encontrada=False
    try:
        with open("lojas.txt","r") as arquivo:
            for linha in arquivo:
                nome_loja,jogo_principal,tipo_item=linha.strip().split("|")
                if nome_loja.lower()==busca.lower():
                    print(f"Loja:{nome_loja}")
                    print(f"Jogo principal:{jogo_principal}")
                    print(f"Item:{tipo_item}")
                    encontrada=True
    except FileNotFoundError:
        print("Local não encontrado!")
        return
    if encontrada==False:
        print("Não achou.")    


def alterar_lojas():
    try:
        print("====== ALTERAR LOJAS ======")
        with open("lojas.txt","w") as arquivo:
               linhas = arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhuma loja cadastrada.")
            return
        posicao = int(input("\nQual registro deseja alterar? "))
        if posicao < 1 or posicao > len(linhas):
            print("Posição inválida.")
            return
        nome_loja = input("Novo nome: ")
        jogo_principal = (input("Novo item: "))
        tipo_item = (input("Nova jogo principal: "))
        linhas[posicao - 1] = f"{nome_loja};{jogo_principal};{tipo_item}"
        with open("lojas.txt", "w") as arquivo:
            arquivo.writelines(linhas)
            print("Registro alterado com sucesso!")

    except FileExistsError:
        print("")
    
def excluir_lojas():
    print("\n====== EXCLUIR lojas ======")
    try:
        with open("lojas.txt","r") as arquivo:
            linhas=arquivo.readlines()
        if len(linhas) == 0:
            print("Nenhuma loja cadastrado no sistema.")
            return
        listar_lojas()
        posicao=int(input("Qual loja deseja excluir: "))       
        if posicao <1 or posicao > len(linhas):
            print("Posição invalida.")
            return
        del linhas[posicao-1]
        with open("lojas.txt","w") as arquivo:
            linhas=arquivo.writelines(linhas)
        print("loja excluido com sucesso!")
    except FileNotFoundError:
        print("Arquivo nãoe contrado!")
    except ValueError:
        print("Digite um valor valido na lista")


def menu_lojas():
    while True:
        print("====== MENU LOJAS ======")
        print("1)Listar lojas\n2)Consultar lojas\n3)Alterar\n4)Excluir lojas\n5)Sair")
        ops_loja=input("Qual opção deseja: ")

        if ops_loja=="1":
            listar_lojas()
        elif ops_loja=="2":
            consultar_lojas()
        elif ops_loja=="3":
            alterar_lojas()
        elif ops_loja=="4":
            excluir_lojas()
        elif ops_loja=="5":
            cadastros()



cadastros()