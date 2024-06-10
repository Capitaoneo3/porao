lista = ["tonny","albert","richard","mordecai","rodolfo","matias","guilherme","jonivaldo","péti"]

def zera_lista():
    global lista
    print(lista)
    if len(lista) >0:
        lista.pop()
        zera_lista()
    else:
        print("a lista está vazia.")

zera_lista()