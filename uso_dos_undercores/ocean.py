class Ocean:
    def __init__(self,sea_creature_name,sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_age

    def __str__(self):
        return f"the creature type is {self.name} and the age is {self.age}"#formatar de um jeito amigável para o usuário ler
    def __repr__(self):
        return f"Ocean({self.name},{self.age})"#formatar de um jeito técnico para o programador ler
    
obj = Ocean("Golfinho",15)

print("__str__() string: ", obj.__str__())#jeito errado de chamar
print("str() string: ", str(obj))#jeito certo de chamar Dunders

print("__repr__() string: ", obj.__repr__())#jeito errado de chamar
print("repr() string: ", repr(obj))#jeito certo de chamar Dunders