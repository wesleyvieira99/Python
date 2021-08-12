# -*- coding: utf-8 -*-
"""
módulos random

"""

#Primeira forma de importação:
import random

#Segunda forma de importação:

from random import random

#uniform() - gerar um numero aleatório entre os valores estabelecidos

from random import uniform
for i in range(10):
    print(uniform(3,7))
    
#Código acima eu imprimo n• aleatório entre 3 e 7, sem incluir o 7, 10 vezes.
    
#randint:

from random import randint
for i in range(6):
    print(randint(1,61))

#choice:
from random import choice
casal_mais_lindo_do_mundo = ['Michael', 'Wesley']
print(choice(casal_mais_lindo_do_mundo))