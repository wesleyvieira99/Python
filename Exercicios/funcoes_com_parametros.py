# -*- coding: utf-8 -*-
"""
Funções com parâmetros

"""

def quadrado(numero):
    return numero **2

print(quadrado(7))
print(quadrado(10))


#Argumentos Nomeados (KeyWords Args): Caso utilizemos nomes dos 
#parâmetros definidos nos argumentos informados, podemos utilizar 
# ordem.

def darnome(nome,sobrenome):
    return f'{nome } {sobrenome}'

print(darnome(nome='Angelina',sobrenome='Jolie'))
print(darnome(sobrenome='Vieira',nome='Wesley'))