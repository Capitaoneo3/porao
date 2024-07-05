import os
print("este é um programa que deixa você escrever em uma arquivo, algumas frases poéticas.")

def  recursiva():
    entrada = str(input("digite uma frase poética."))
    if entrada == "":
        print("você saiu por não escrever uma frase poética.")
        arquivo = open("atividade_escrita/frases.txt","r")
        print(arquivo.read())
        arquivo.close()
        pass #avisa pra recursiva que nao vai dar em nada e sai

    if os.path.exists("atividade_escrita/frases.txt"):
        arquivo = open("atividade_escrita/frases.txt","a")
    else:
        arquivo = open("atividade_escrita/frases.txt","w")
    arquivo.write(f"{entrada}\n")
    arquivo.close()
    recursiva()

recursiva()