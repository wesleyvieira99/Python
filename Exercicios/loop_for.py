# -*- coding: utf-8 -*-
"""
Estruturas de repetição: Loop For.


"""

nome = 'Geek University'
lista = [1, 3 ,5 ,7 ,9]
numeros = range(1,10)


# Exemplo de FOR 1 (iterando sobre uma String):

for letra in nome:
    print(letra)


# Exemplo de FOR 2 (iterando sobre uma lista):

for numero in lista:
    print(numero)


# Exemplo de FOR 3 (iterando sobre um range) :
    
for numero in range(1,10):
    print(numero)
    
for i, v in enumerate(nome):
    print(nome[i])

'Este enumerate faz com que as letras da String'
'Sejam atreladas a índices ([0], [1], e assim por diante'
'Ou seja, para cada sequência de nosso iterável ele atrela a um índice'




'Imprimindo uma iteração na mesma linha'
nome = 'Geek University'
for letra in nome:
    print(letra, end='')