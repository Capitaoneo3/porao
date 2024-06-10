lista = ["tonny","albert","richard","mordecai","rodolfo","matias","guilherme","jonivaldo","péti"]

def zera_lista(l:list):
    
    print(l)
    if len(l) >0:
        l.pop()
        zera_lista(l)
    else:
        print("a lista está vazia.")

zera_lista(lista)