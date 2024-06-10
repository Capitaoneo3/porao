a = ["apple","banana"]
b = ["ford","BMW"]


#no final das contas foi inserido um novo item no final da lista a 
#e o valor desse novo item é a lista de b como podemos ver no console 
for item in b:
    a.append(item)

print(a)