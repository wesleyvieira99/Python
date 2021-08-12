# -*- coding: utf-8 -*-
"""
MAP

"""
import math

def area(r):
    """Calcula a area de um círculo com um raio r"""
    return math.pi * (r ** 2)

print(area(2))


raios = [2, 5, 7, 8.6]

#Forma comum

areas = []
for r in raios:
    areas.append(area(r))

print(areas)

#Forma com map

areas = map(area, raios)
print(list(areas))

#Forma map com lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))


#mais um exemplo

cidades = [('São Paulo', 20), ('Limeira', 30,)]

c_para_f = lambda dado: (dado[0], dado[1] * 10)

print(list(map(c_para_f, cidades)))