# -*- coding: utf-8 -*-
"""
Generetors

"""
# Como list comprehension:

nomes = ['Wesley', 'Wes', 'We']

print(any([nome[0] == 'W' for nome in nomes]))

# Sem list comprehension:

nomes = ['Wesley', 'Wes', 'We']

print(any(nome[0] == 'W' for nome in nomes))

