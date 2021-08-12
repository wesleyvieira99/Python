# -*- coding: utf-8 -*-
"""
Módulo Collections: Counter
"""


#*Counter - Exemplo 1

from collections import Counter
#Importando o Counter


lista = [1,1,1,2,2,3,3,3,3,1,1,1,4,4,5,5,1,1,2,2,3,3,5,4]
#Aqui podemos utilizar qualquer iterável, aqui usamos uma lista


res = Counter(lista) 
 #Utilizando o Counter

print(type(res))
print(res)

#*Counter - Exemplo 2

print(Counter('Geek University'))

#*Counter - Exemplo 3

texto = """ Texto grande Texto Texto Texto Texto 
grande grande
grande grande grande grande grande grande]
Texto Texto Texto Texto Texto Texto Texto Texto
grande grande grande grande grande grande grande[]
Texto Texto Texto Texto Texto Texto wej Texto
grande grande grande grande grande grande grande """

palavras = texto.split()
print(palavras)

res = Counter(palavras)
print(res)

print(res.most_common(5))
#Encontrando as cinco palavras com mais ocorrência no texto