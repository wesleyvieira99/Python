# -*- coding: utf-8 -*-
"""
Funções que retornam valores

"""

def quadrado_de_sete():
    print(7*7)
    
quadrado_de_sete()

#A função acima não retorna o resultado da operação e sim somente imprime

lista = [1,2,3]

print(len(lista))
#A função Len acima retorna valor (quantidade de itens da lista)
#Em python, quando uma função não retorna nenhum valor, o retorno é 
#dado como None.

#Funções Python que retornam valores, devem retornar estes valores 
#com a palavra reservada “return”:
def quadrado_de_sete():
    return 7*7
    
quadrado_de_sete()

#Return finaliza a função, ou seja, ela sai da execução da função.
def diz_oi():
    return 'oi'
    print('estou sendo executado após o retorno')

print(diz_oi())

#Podemos ter em uma função com diferentes “returns”, ou seja,
#em uma função podemos ter mais de um return, porém a função somente
#retornará um deles.
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 5


#Podemos, em uma função, retornar qualquer tipo de dado e até 
#mesmo múltiplos valores.
def outra_funcao():
    return 2,3,4,5

num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)

#Vamos criar uma função para jogar cara e coroa
from random import random
#Numero aleatório entre 0 e 1

def joga_moeda():
    valor = random()
    if valor > 0.5:
        print(valor)
        return 'cara'
    print(valor)
    return 'coroa'

print(joga_moeda())

    


