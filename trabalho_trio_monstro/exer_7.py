import time
def ver_feed_bek():
        try:
                with open("feed_bek.txt", "r") as arquivo:
                    linhas = arquivo.readlines()
                if len(linhas) == 0:
                    print("Nenhum feed-bek cadastrada.")
                    return
                print("\n===== LISTA DE ENTREGAS ======")
                for posicao, linha in enumerate(linhas, start=1): 
                    feed_b = linha.strip().split(";")
                    print(f"{posicao} - {feed_b}")
        except FileNotFoundError:
                print("nenhum feed bek encontrado, você não e famoso melhore 😒")
def dar_feed_bek():
        with open("feed_bek.txt","a") as arquivo:
            feed_b = input("feed bek: ")
            arquivo.write(f"{feed_b} \n")
        print("Entrega de feed-bek com sucesso!")
def feed_bek():     
    while True:
        print("=====--            --=======")
        print("=====--VER FEED BEK--=======")
        print("=====--DAR FEED BEK--=======")
        print("=====--            --=======")

        ops_fed=int(input("qual gostaria de conferir: "))

        if ops_fed=="1":
            dar_feed_bek()
        elif ops_fed=="2":
            ver_feed_bek()
        else:
            print("opsão invalida ")
            time.sleep(0.7)
            return