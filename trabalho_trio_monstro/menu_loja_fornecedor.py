import time
import os


def alterar_iten():
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

def excluir_iten():
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
        nome_jogo= input("Novo nome: ")
        categoria_jogo= input("Nova quantidade: ")
        linhas[posicao - 1] = f"{nome_jogo};{categoria_jogo}"
        with open("usuarios.txt", "w") as arquivo:
            arquivo.writelines(linhas)
            print("Registro alterado com sucesso!")

    except FileExistsError:
        print("")
    
def cadastro_itens():
    print("======== 🎮 CADASTROS 🎮 ========")
    categoria_jogo=input("qual o genero ?")
    nome_jogo=input("qual o nome do jogo ? ")
    with open("entregas.txt", "a") as arquivo:
       arquivo.write(f"{nome_jogo};{categoria_jogo}\n")
    print("cadastrado com sucesso ? ")

while True:
    print("=====----                ----=====")
    print("=====---- CADASTRAR ITEM ----=====")
    print("=====---- EXCLUIR ITEM   ----=====")
    print("=====---- ALTERAR ITEM   ----=====")
    print("=====----                ----=====")

    ops_loja=int(input("qual opsõa deseja: "))

    if ops_loja=="1":
        cadastro_itens()
    elif ops_loja=="2":
        excluir_iten()
    elif ops_loja=="3":
        alterar_iten()
        

        
