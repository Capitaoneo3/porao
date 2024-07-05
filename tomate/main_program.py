class Tomate:
    def __init__(self, color, sabor):#esse tomate recebe cor e sabor.
        self.color = color
        self.sabor = sabor#esse tomate não tem métodos
    def __repr__(self):#sempre criar o repr de uma classe
        return f"tomate({self.color},{self.sabor})"

def salva_lista_tomate(lista:list):
    with open('tomate/tomates.txt', 'w') as file:#with cria um alias apelido para o arquivo tomates.txt
         #dizendo que vamos nos referir ao arquivo como a variável file. w significa modo de escrita, pois quero
        #escrever uma lista de tomates no arquivo.
        for tomate in lista:
            file.write(f'Color: {tomate.color}, Sabor: {tomate.sabor}\n')#\n dá uma quebra de linha.








def carrega_lista_tomate():
    with open('tomate/tomates.txt', 'r') as file:#whit alias novamente para variável file.
        lines = file.readlines()#a variável lines tem o valor de lista onde
        #cada item é uma linha do arquivo
    for line in lines:# line representa uma linha das lines.
        data = line.strip().split(', ')#usamos o strip para remover caracteres especiais com o /n
        #e o split para dividir os valores depois da string "', '".
        color = data[0].split(': ')[1]
        sabor = data[1].split(': ')[1]
        tomate = Tomate(color, sabor)#o que está havendo aqui?
        list_tomate.append(tomate)#adicionar um tomate na lista de tomate
        #assim é carregado os tomates para a variável list_tomate.

    for tomate in list_tomate:
        print(f'Color: {tomate.color}, Sabor: {tomate.sabor}')


tomate1 = Tomate('verde', 'dulce')
tomate2 = Tomate('rojo', 'agrio')

list_tomate = []
carrega_lista_tomate()
print(list_tomate)
#salva_lista_tomate(list_tomate)

