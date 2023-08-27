#!/bin/python3

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    # Uma forma de acessar os likes a partir de .likes sem a necessidade do uso de ()
    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    # Uma forma de acessar o nome a partir de .nome sem a necessidade do uso de ()
    @property
    def nome(self):
        return self._nome
    
    # Uma maneira de alterr o nome a partir de ".nome = 'novo_nome'" ao invés de .nome('novo_nome')
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    # Uma representação textual do objeto programa
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes'
