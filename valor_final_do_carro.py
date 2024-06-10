v_fabrica = float(input("digite o valor de fábrica do auto para informarmos o valor final para o consumidor."))

def calc_imposto_distribuidor():
    global v_fabrica
    v_com_imposto_distribuidor = v_fabrica+(v_fabrica*0.28)

    return v_com_imposto_distribuidor

def calc_impostos_gov(v):
    v += v*0.45
    return v
v_atualizado = calc_imposto_distribuidor()
v_atualizado = calc_impostos_gov(v_atualizado)

print(f"O auto de valor de fábrica:R${v_fabrica}, fica com um valor total ao consumidor de:R${v_atualizado}")


