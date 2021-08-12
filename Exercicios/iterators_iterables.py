# -*- coding: utf-8 -*-
"""
Entendendo Iterators e Itarables

"""
#Iteráveis - Iterable:
nome = 'Geek'
numeros = [1,2,3,4,5,6]

#Transformando iteráveis em iterator usando a função iter()

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))


