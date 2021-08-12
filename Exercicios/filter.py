# -*- coding: utf-8 -*-
"""
FILTER

"""

import statistics

dados = [1,2,3,4,5,6]
media = statistics.mean(dados)

print(media)

res = filter(lambda x: x > media, dados)
print(list(res))


paises = ['','BR', 'EUA', '']

print(list(filter(lambda x: x != '', paises )))



