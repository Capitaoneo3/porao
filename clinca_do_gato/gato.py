class Gato:
    def __init__(self,name,idade,peso,raca,cor):
        self.name =  name
        self.idade = idade
        self.peso = peso
        self.raca = raca
        self.cor = cor
    def __repr__(self):
        return f"Gato(nome:{self.name};idade:{self.idade};peso:{self.peso};raca:{self.raca};{self.cor})"
    