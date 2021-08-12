# -*- coding: utf-8 -*-
"""
List Comprehensions - Parte 1
Os list comprehensions, utilizando ela, nós podemos gerar novas
listas com dados processados a partir de outro iterável. 

#Sintaxe da List Comprhensions:

[ dado for item in iterável ]
Ou seja eu tenho uma coleção de dados (iterável) e para cada 
item nesta coleção faz uma nova lista
"""

numeros = [1,2,3,4,5]

res = [numero * 10 for numero in numeros]
#multiplique cada número por 10 na coleção numeros
print(res)

def funcao (valor):
    return valor * valor

res = [funcao(valor) for valor in numeros]

print(res)

#Com Strings

nome = 'wesley'

print([letra.upper() for letra in nome])

#Usando o range

print([numero * 3 for numero in range(1,10)])
    
"""
List Comprehensions - Parte 2

Nós podemos adicionar estruturas condicionais lógicas às nossas List
Comprehension

"""

#1

numeros = [1,2,3,4,5]

pares = [numero for numero in numeros if numero % 2 == 0]
print (pares)

#2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)