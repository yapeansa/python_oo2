#!/bin/python3

# from abc import ABC Abstract Base Classes

# from collections.abc import MutableSequence
from numbers import Complex

class Numero(Complex):
    def __getitem__(self, item):
        super().__getitem__(item)

filmes = Numero()
