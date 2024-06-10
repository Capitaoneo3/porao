TEMPO_CONTRI_MAXIMO = 40
sexo = str(input("digite M para masculino ou F para feminino"))
idade_contri_inicial = int(input("Com qual idade você começou a contribuir?"))
idade_contri_projetada_m = 65 - idade_contri_inicial
idade_contri_projetada_f = 62 - idade_contri_inicial

def print_tempo_faltando_homem():
    print("você terá direito a se aposentar com 65 anos")
    print(f"Você precisa trabalhar até os {tempo_faltando_contri_homem()} anos para conseguir 100%")
def print_tempo_faltando_mulher():
    print("você terá direito a se aposentar com 62 anos")
    print(f"Você precisa trabalhar até os {tempo_faltando_contri_mulher()} anos para conseguir 100%")
def tempo_faltando_contri_homem():
    global TEMPO_CONTRI_MAXIMO
    global idade_contri_projetada_m
    idade_contri_projetada_m_faltando = (TEMPO_CONTRI_MAXIMO - idade_contri_projetada_m)+65
    return idade_contri_projetada_m_faltando

def tempo_faltando_contri_mulher():
    global TEMPO_CONTRI_MAXIMO
    global idade_contri_projetada_f
    idade_contri_projetada_f_faltando = (TEMPO_CONTRI_MAXIMO - idade_contri_projetada_m)+62
    return idade_contri_projetada_f_faltando

def calc_contri_homem():
    global idade_contri_projetada_m
    if idade_contri_projetada_m >=25 and idade_contri_projetada_m <=29:
        print(f"você tem{idade_contri_projetada_m} anos de contribuição, o que te dá direito a 70% sobre o beneficio")
        print_tempo_faltando_homem()
    elif idade_contri_projetada_m >=30 and idade_contri_projetada_m <=34:
        print(f"você tem{idade_contri_projetada_m} anos de contribuição, o que te dá direito a 77,5% sobre o beneficio")
        print_tempo_faltando_homem()
    elif idade_contri_projetada_m >=35 and idade_contri_projetada_m <=39:
        print(f"você tem{idade_contri_projetada_m} anos de contribuição, o que te dá direito a 87,5% sobre o beneficio")
        print_tempo_faltando_homem()
    elif idade_contri_projetada_m >=40:
        print(f"você tem{idade_contri_projetada_m} anos de contribuição, o que te dá direito a 100% sobre o beneficio")
        print_tempo_faltando_homem()
    else:
        print(f"so sorry, você não atingiu o tempo mínimo de contribuição. Seu tempo de contribuição foi:{idade_contri_projetada_m} anos")
        print_tempo_faltando_homem()    

def calc_contri_mulher():
    global idade_contri_projetada_f
    if idade_contri_projetada_f >=25 and idade_contri_projetada_f <=29:
        print(f"você tem{idade_contri_projetada_f} anos de contribuição, o que te dá direito a 70% sobre o beneficio")
        print_tempo_faltando_mulher()
    elif idade_contri_projetada_f >=30 and idade_contri_projetada_f <=34:
        print(f"você tem{idade_contri_projetada_f} anos de contribuição, o que te dá direito a 77,5% sobre o beneficio")
        print_tempo_faltando_mulher()        
    elif idade_contri_projetada_f >=35 and idade_contri_projetada_f <=39:
        print(f"você tem{idade_contri_projetada_f} anos de contribuição, o que te dá direito a 87,5% sobre o beneficio")
        print_tempo_faltando_mulher()        
    elif idade_contri_projetada_f >=40:
        print(f"você tem{idade_contri_projetada_f} anos de contribuição, o que te dá direito a 100% sobre o beneficio")
        print_tempo_faltando_mulher()        
    else:
        print(f"so sorry, você não atingiu o tempo mínimo de contribuição. Seu tempo de contribuição foi:{idade_contri_projetada_f} anos")
        print_tempo_faltando_mulher()        



if sexo == "m" or sexo == "M":
    calc_contri_homem()
elif sexo == "f" or sexo == "F":
    calc_contri_mulher()
else:
    print("você digitou errado as opções.")