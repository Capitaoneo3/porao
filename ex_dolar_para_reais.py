dolares = float(input("quantos dolares você quer trocar por reais? "))
coatacao = float(input("qual a cotação do dolar hoje? "))

def conversao_dolar_reais(d,c):
    return dolares*coatacao

conversao = conversao_dolar_reais(dolares,coatacao)

print(f"o valor de $US{dolares} ficaria R${conversao} em reais")