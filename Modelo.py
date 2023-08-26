#!/bin/python3

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.likes} Likes')

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes')

vingadores = Filme('vingadores: guerra infinita', 2018, 160)

atlanta = Serie('atlanta', 2018, 2)

series_e_filmes = [vingadores, atlanta]

for i in range(0, 5):
    vingadores.dar_like()
    atlanta.dar_like()

for programa in series_e_filmes:
    programa.imprime()
