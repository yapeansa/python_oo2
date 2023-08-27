#!/bin/python3

from Modelo import *

vingadores = Filme('vingadores: guerra infinita', 2018, 160)

atlanta = Serie('atlanta', 2018, 2)

series_e_filmes = [vingadores, atlanta]

for i in range(0, 5):
    vingadores.dar_like()
    atlanta.dar_like()

for programa in series_e_filmes:
    print(programa)
