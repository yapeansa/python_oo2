#!/bin/python3

from modelo import *

# Criamos a seguir um objeto filme e um objeto série

vingadores = Filme('vingadores: guerra infinita', 2018, 160)

atlanta = Serie('atlanta', 2018, 2)

# Em cada um dos objetos, atribuímos 5 likes

for i in range(0, 5):
    vingadores.dar_like()
    atlanta.dar_like()

# Organizamos os objetos em uma lista

series_e_filmes = [vingadores, atlanta]

# Exibimos as representações textuais dos objetos

for programa in series_e_filmes:
    print(programa)
