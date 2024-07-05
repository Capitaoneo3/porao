class Usuario:
    def __init__(self,nome,senha):#6
        self.nome = nome
        self.senha = senha

    def __repr__(self):
        return f"{self.nome},{self.senha}"
    
    @staticmethod
    def from_string(user_str):#7
        nome , senha = user_str.split(',')
        return Usuario(nome,senha)