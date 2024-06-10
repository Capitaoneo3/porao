def calc_pag_funcionario():    
    nome = input("digite o nome do funcionário ")
    total_vendas = float(input(f"digite o total de vendas do {nome}"))
    salario_base = float(input(f"digite o salário base do {nome}"))
    

    comissao = calc_comi_15porcento(total_vendas)

    print("o salário base de",nome,"é:",salario_base,"e sua comissão foi de:",comissao,".")
    print("gerando um total de",salario_base+comissao)

def calc_comi_15porcento(a):
    return a*0.15

calc_pag_funcionario()
calc_pag_funcionario()