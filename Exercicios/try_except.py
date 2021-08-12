# -*- coding: utf-8 -*-
"""
Try Excepet

"""

#Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print("Não dá para executar uma função sem definir")
    
#Exemplo 2 - Tratando erro de forma específica
    
try:
    geek()
except NameError as err:
    print(f'A aplicaçõa gerou o seguinte erro: {err}')

