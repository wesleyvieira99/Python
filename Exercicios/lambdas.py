# -*- coding: utf-8 -*-
"""
Utilizando lambdas

"""
#Expressão Lambda
lambda x: 3 * x + 1
#Parâmetro é o x, retorno vem depois dos dois pontos

#Utilizando a expressão lambda

calc = lambda x: 3 * x + 1 

print(calc(5))

#Podemos ter expressões lambdas com múltiplas entradas:

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

#Definindo uma função quadrática
#Uma função com uma lambda dentro

def funcao_quadratica(a,b,c):
    return lambda x: a * x ** 2 + b * x + c

teste = funcao_quadratica(2, 3, -5)

#Definindo o valor de x da lambda
print(teste(0))

print(funcao_quadratica(3,0,1)(2))