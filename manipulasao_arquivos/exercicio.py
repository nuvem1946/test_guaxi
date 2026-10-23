import os
import time

def limpar_sugeira():
    os.system("cls")

def cadastrar():
    print("========------CADASTRO-------========")
    marca=input("digite a desenvolvedora: ")
    data_validos=["2020","2021","2022","2023","2024","2025","2026"]
    while True:
        
        tamanho=input("digite o ano que foi lançado o jogo ").strip().upper()
        if tamanho in data_validos:
            with open("jogos.txt","w") as arquivos:
                nome_jogo=print("qual nome do seu jogo: ")
                categoria_jogo=print("qual categoria do seu jogo: ")
            break
        else:
            print("data invalido: digite o ano que foi lançado o jogo")

    with open("jogo.txt","a") as arquivos:
            arquivos.write(f"{marca};{tamanho}\n")
    print("\nCADASTRANDO...")
    time.sleep(1.5)
    print("\nCADASTRO REALIZADO!")
    time.sleep(1.5)

def lita():
    print("======------LISTA-----======")
    try:
        with open("jogo.txt","r") as arquivos:
            linhas=arquivos.readlines()
            if len(linhas)==0:
                print("nada cadastrado ou encontrado")
            else:
                for posicao,linhas in enumerate(linhas,start=1):
                    marca,tamanho=linhas.strip().split(";")
                    print(f"{posicao}-{marca}|{tamanho}  ヾ(•ω•`)o")
    except FileExistsError:
        print("arquivo não encontrado | ┬┬﹏┬┬ |")
    input("\n precione qualquer tecla para voltar ao menu....")
    return
def alterar():
    print("=====-----ALTERAR----=====")
    try:
        with open("jogos.txt","r") as arquivos:
            linhas = arquivos.readlines()
            if len(linhas) == 0:
                print ("Nenhuma jogo cadastrada!@#!")
                return
            posicao = int(input("Qual jogo deseja alterar? "))
            if posicao < 1 or posicao > len(linhas):
                print("Posição Inválida!")
                return
            novo_nome_jogo=input("qual seu novo jogo: ")
            nova_categoria_jogo=input("qual sua nova categoria: ")   
            linhas[posicao-1]=f"{novo_nome_jogo};{nova_categoria_jogo}" 
            with open("jogo.txt","r") as arquivos:
                arquivos.writelines(linhas)
            print("---jogo alterrado---")

    except EnvironmentError:
        print("jogo não encontrado| cadastre um jogo ")
        return
    time.sleep(0.5)

def excluir():
    print("============-------EXCLUIR---------========")
    lita()
    try:
            with open("jogos.txt","r") as arquivos:
                        linhas = arquivos.readlines()
                        if len(linhas) == 0:
                            print ("Nenhuma jogo cadastrada!@#!")
                            return
                        posicao = int(input("Qual jogo deseja alterar? "))
                        if posicao < 1 or posicao > len(linhas):
                            print("Posição Inválida!")
                            return
                        del linhas[posicao-1]
                        with open("jogo.txt","w") as arquivos:
                            linhas= arquivos.writelines(linhas)
                            print("jogo excluido com sucesso..") 
                            time.sleep(0.5)
    except FileNotFoundError:
            print("jogo não encontrado")
while True:
    limpar_sugeira()
    print("=====-----MENU---=====")
    print("          MENU")
    print("1-cadastrar jogo")
    print("2-listar")
    print("3-alterar")
    print("4-excluir")
    print("0-sair")

    opc=int(input("qual opsão deseja: "))

    match opc:
        case 1:
            print("iniciando cadastro...")
            time.sleep(0.7)
            cadastrar()
        case 2:
            print("verificando lista..")
            time.sleep(0.8)
            lita()
        case 3:
            print("indo alterrar")
            time.sleep(0.5)
            alterar()
        case 4:
            excluir()
        case 0:
            print("saindo do programa..")
            time.slep("0.9")
            break
        case _:
            print("opção invalida!")
            time.slep(1.0)