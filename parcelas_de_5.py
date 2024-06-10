print("bem vindo a loja mamão com açucar.\n Abaixo digite o valor total da compra para parcelar ela em 5 vezes")
total_compra=float(input("valor da compra: "))

def v_parcelas_de_5_meses(v):
    v_r = v/5
    return v_r
v_qnt_parcelas = v_parcelas_de_5_meses(total_compra)
print(f"esse valor R${total_compra} parcelado em 5x ficaria R${v_qnt_parcelas}")