#!/bin/python3

from programas import *

# Criamos a seguir um objeto filme e um objeto série

vingadores = Filme('vingadores: guerra infinita', 2018, 160)

atlanta = Serie('atlanta', 2018, 2)

tmep = Filme('Todo mundo em pânico', 1999, 100)

demolidor = Serie('Demolidor', 2016, 2)

# Em cada um dos objetos, atribuímos 5 likes

for i in range(0, 5):
    vingadores.dar_like()
    atlanta.dar_like()
    tmep.dar_like()
    demolidor.dar_like()

# Organizamos os objetos em uma lista

series_e_filmes = [vingadores, atlanta, tmep, demolidor]

# criamos o objeto Playlist

playlist_fim_de_semana = Playlist('fim de semana', series_e_filmes)

# Exibimos as representações textuais dos objetos

for programa in playlist_fim_de_semana.listagem:
    print(programa)

# Imprimindo o tamanho da Playlist

print(f'Tamanho da Playlist: {len(playlist_fim_de_semana.listagem)}')
