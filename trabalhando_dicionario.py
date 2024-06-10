#Título;Autor;Ano de lançamento;Favorito
livros = [{"titulo":"Dom Quixote","autor":"Miguel de Cervantes","ano_lanc":1612,"favorito":0},
          {"titulo":"Um Conto de Duas Cidades","autor":"Charles Dickens","ano_lanc":1859,"favorito":0},
          {"titulo":"O Pequeno Príncipe","autor":"Antoine de Saint-Exupéry","ano_lanc":1943,"favorito":0},
]
"""
livro_fav = livros[2]

livro_fav["favorito"]=1

livros[2] = livro_fav

print(livros)
"""

for livro in livros:
    if livro["titulo"] == "O Pequeno Príncipe":
        livro["favorito"]=1

print(livros)