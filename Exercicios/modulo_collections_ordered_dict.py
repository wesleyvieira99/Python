# -*- coding: utf-8 -*-
"""
Módulo Colletions
Ordered Dict
"""

dicionario = {'a': 1, 'b': 2, 'c': 3}


from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3})

for chave, valor in dicionario.items():
    print(f'chave: {chave}, valor:{valor}')
