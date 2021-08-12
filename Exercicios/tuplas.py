# -*- coding: utf-8 -*-
"""

Tuplas (tuples)

"""
#Cuidado 1: Tuplas são representadas por parêntes. Mas veja:

tupla1 = (1,2,3,4)
print(type(tupla1))
print(tupla1)

tupla2 = 1,2,3,4,5,6
print(tupla2)
print(type(tupla2))

#Quando eu coloco em uma variável uma sequência por vírgula, o Python considera 
#como se fosse uma tupla

#Cuidado 2: Tuplas com um elemento:

tupla3 = (4)
print(tupla3)
print(type(tupla3))

#Neste caso quando colocamos uma tupla com somente um elemento, é um int e 
#não uma tupla, neste caso.


tupla4 = (4,) #Isso é uma tupla, mesmo que esteja com o segundo elemento vazio

print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Transformando um range em um tupla:
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

#Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python')
escola, curso = tupla
print(escola)
print(curso)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Métodos para adição e remoção de elementos nas tuplas não existem dado o fato delas
#Serem imutáveis.
#Soma, valor máximo, mínimo e tamanho valem a mesma coisa. Se o números forem int e reais.

tupla = (1,2,3,4,5,6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Concatenação de tuplas
tupla1 = 1,2,3
print(tupla1)
tupla2 = 4,5,6
print(tupla2)
print(tupla1+tupla2)
print(tupla1)
print(tupla2)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Verificar se determinado elemento está contido na tupla

tupla = 1,2,3
print(3 in tupla)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Iterando sobre um tupla:

tupla = 1,2,3
for n in tupla:
    print(n)
    
for indice, valor in enumerate(tupla):
    print(indice,valor)
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Contando elementos dentro de uma tupla:
tupla = ('a','b','c','d','a','b')
print(tupla.count('b'))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Dicas na utilização de tuplas:

#1. Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção;
#2. O acesso a elementos de uma tupla também é semelhante a uma lista;
#3. Com esse acesso via índice podemos iterar com o While.
