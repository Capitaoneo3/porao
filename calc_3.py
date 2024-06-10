n1 = int(input("digite o primeiro número"))
n2 = int(input("digite o segundo número"))

print("escolha uma opção: [1]média entre os números digitados\n[2]Diferença entre os números digitados")
print("escolha uma opção: [3]produto entre os números digitados\n[4]Divisão entre os números digitados")

escolha = int(input(": "))
media = (n1+n2) / 2
diferenca = n1-n2
produto = n1*n2
divisao = n1/n2
match escolha:
    case 1:
        print(f"a média entre os números digitados é {media}")
    case 2:
        print(f"a Diferença entre os números digitados é {diferenca}")
    case 3:
        print(f"o produto entre os números digitados é {produto}")
    case 4:
        print(f"a divisao entre os números digitados é {divisao}")
    case _:
        print("opção inválida")