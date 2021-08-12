# -*- coding: utf-8 -*-
"""
Módulo Collections
Named Tuples
"""

#Recaptulando as tuplas
tupla =(1, 2, 3)
print(tupla[1])

#Agora veremos sobre o Named Tuple

from collections import namedtuple
#improtação

cachorro = namedtuple('cachorro', 'idade, raca, nome')
#definir nomes e parâmetros, declaração namedTUple
#'cahorro' é o nome da tupla e 'idade, raca, nome' os parâmetros da tupla

ray = cachorro(idade=2, raca='shawshaw', nome='Ray')
print(ray)
#usando agora

print(ray[0])
print(ray[1])
print(ray[2])


print(ray.idade)
print(ray.raca)
print(ray.nome)


