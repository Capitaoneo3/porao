ordem = 0
lista = [10]


while ordem != 2:
    num = int(input('Digite a 1º numero: '))
    lista.append(num)
    ordem +=1

print (f'Lista na ordem em que foi digitada {lista}')
lista.reverse()
print (f'Lista reversa: {lista}')