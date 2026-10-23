import os
import time

def limpar_sugeira():
    os.system("cls")

def cadastrar():
    print("========------CADASTRO-------========")
    marca=input("digite a marca da roupa: ")
    tamanhos_validos=["PP","P","M","MG","G","GG","GAY"]
    while True:
        
        tamanho=input("digite o tamanho (PP/P/M/MG/G/GG) ").strip().upper()
        if tamanho in tamanhos_validos:
            break
        else:
            print("tamanho invalido: digite o tamanho (PP/P/M/MG/G/GG) ")

    with open("vestuario.txt","a") as arquivos:
            arquivos.write(f"{marca};{tamanho}\n")
    print("\nCADASTRO...")
    time.sleep(1.5)
    print("\nCADASTRO REALIZADO!")
    time.sleep(1.5)

def lita():
    print("======------LISTA-----======")
    try:
        with open("vestuario.txt","r") as arquivos:
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

while True:
    limpar_sugeira()
    print("=====-----MENU---=====")
    print("          MENU")
    print("1-cadastrar roupa")
    print("2-listar")
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
        case 0:
            print("saindo do programa..")
            time.slep("0.9")
            break
        case _:
            print("opção invalida!")
            time.slep(1.0)