nomes = []

def verifica_se_esta_na_lista(string_):
    global nomes
    if string_ in nomes:
        print(f"o nome {string_} está na lista:\n {nomes}")
    else:
        print(f"o nome {string_} não está na lista:\n {nomes}")   


for i in range(0,4):
    entrada = input(f"{i}: digite um nome: ")
    nomes.append(entrada)

ultima_entrada = input("Agora digite um nome para ver se está na lista: ")

verifica_se_esta_na_lista(ultima_entrada)

