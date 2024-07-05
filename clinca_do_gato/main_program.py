from gato import  Gato

def cadastra_gato(gato:Gato):
    with open('clinca_do_gato/dados.txt', 'w') as file:
        file.write(repr(gato)+"\n")

gato1 = Gato("julian","15","2","Siamês","cinza com preto")

#cadastra_gato(gato1)
def le_gato():
    usuarios = []
    tarefas = []
    try:
        with open('projeto/dados.txt', 'r') as file:
            for line in file:
                line = line.strip()
           
               
    except FileNotFoundError:
        pass
    return usuarios, tarefas