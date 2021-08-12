# -*- coding: utf-8 -*-
"""

Dictionary Comprehensions

Sintaxe:
{chave: valor for valor in iterável}
"""

#Exemplo1
dicionario = {'a': 1, 'b': 2, 'c': 3}

quadrado = {chave + 'b':valor ** 2 for chave, valor in dicionario.items()}

print(quadrado)

#Exemplo2
numero = [1,2,3,4,5]

quadrados = {valor: valor ** 2 for valor in numero}
print(quadrados)

#Exemplo3

chaves = 'abcde'
valores = [1,2,3,4,5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)