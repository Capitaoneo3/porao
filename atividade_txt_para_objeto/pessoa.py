class Pessoa:
    def __init__(self,nome_,idade_,cor_olho_):
        self.nome = nome_
        self.idade = idade_
        self.cor_olho = cor_olho_

    def __repr__(self):
        return f"Pessoa: nome:{self.nome}idade:{self.idade}cor_olho:{self.cor_olho}"