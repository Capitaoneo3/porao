fora = "fora"#global

def inside():
    dentro = "dentro"#local
    print(fora)
    print(dentro)

print(fora)#fora é global e é possível printar ela
#dentro e fora dos blocos
print(dentro)#dentro é var local e só quem está dentro 
#do bloco que consegue acessar ela.