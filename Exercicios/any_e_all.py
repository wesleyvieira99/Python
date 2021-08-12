# -*- coding: utf-8 -*-
"""
Any e All


"""

#Exemplo All()

print(all([0,1,2,3,4])) #Todos os elementos são verdadeiros?

#Checar se todos os usuários da lista começam com a letra C
nomes = ['Camila', 'Caio']

print(all([nome[0] == 'C' for nome in nomes]))

#Exemplo Any()

print(any([1,2,3,4,5]))

