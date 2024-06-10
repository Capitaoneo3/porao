# bebida 80 comida 60 transporte 15
gasto_total = 0

print("custo médio da noite  bebida 80 comida 60 transporte 15 ")
pergunta1_bebida= int(input("deseja beber? [1]para sim e [2]para não "))
if not pergunta1_bebida == 1 and not pergunta1_bebida == 2:
    print("opção inválida")
pergunta2_comida= int(input("deseja comer? [1]para sim e [2]para não "))
if not pergunta2_comida == 1 and not pergunta2_comida == 2:
    print("opção inválida")
pergunta3_transporte= int(input("deseja transporte? [1]para sim e [2]para não "))
if not pergunta3_transporte == 1 and not pergunta3_transporte == 2:
    print("opção inválida")

pergunta4_amigos= int(input("quantas pessoas vão sair com você? "))


def calc_gasto_noite(b,c,t,a):
    global gasto_total
    if b == 1:
        gasto_total += 80
    if c == 1:
        gasto_total += 60       
    if t == 1:
        gasto_total += 15
    if a > 0:
        gasto_total += gasto_total*a+1
calc_gasto_noite(pergunta1_bebida,pergunta2_comida,pergunta3_transporte,pergunta4_amigos)

print(f"o gasto estimado da noite é R${gasto_total}")


        