import random 

numero_sorteado = random.randint(1,10)

numero_do_usuario = None
tentativas = 0

while numero_sorteado != numero_do_usuario:
    numero_do_usuario = int(input("digite um número de 1 a 10: "))
    tentativas += 1
    if numero_do_usuario >=1 and numero_do_usuario <=10:
        if numero_sorteado < numero_do_usuario:
            print("tente um número menor na próxima")
        else:
            print("tente um número maior na próxima")
    else:
        print("valor inválido.")

print("o seu número foi: ",numero_do_usuario, "e o número sorteador foi: ",numero_sorteado,"suas tentativas foram: ",tentativas)