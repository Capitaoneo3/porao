passaros = ["5","3","4","5","2"]
#passaros.insert(6,"angribird_vermelho")#insere esse valor no indice zero, deslocando o valor anterior para direita

print(passaros)
print("  ")
print(" abaixo a lista passaro em ordem crescente: ")
passaros.sort()#não retorna exibição, só usado para manipulação.
print(passaros)


"""
print(passaros)
print("  ")
print(" abaixo a lista passaro em ordem inversa: ")
passaros.reverse()#não retorna exibição, só usado para manipulação.
print(passaros)
"""

"""
if "Beija-flor" in passaros: #usamos o in para localizar um valor na lista.
    print("acharam o beija flor")
else:
    print("o beija flor não está")
"""


passaros.pop(-1) #deleta um indice e o seu valor obviamente.
#print(passaros)


passaros.append("Rolinha")#adiciona esse valor no final da lista.
#print(passaros)

#passaros.remove("papagaio")#remove buscando o valor
#print(passaros)

passaros[0] = "" #atribui um valor ao indice zero ou substitui o anterior



    
