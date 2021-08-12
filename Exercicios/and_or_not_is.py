# -*- coding: utf-8 -*-
"""
Os operadores AND [e] , OR [ou] , NOT [não], IS [é] nas estruturas lógicas

"""


'Para o AND, ambos os valores precisam ser true'
'Para o OR, um dos dois valores precisam ser true'
'Para o NOT, o valor booleano é invertido. Ele é um operador de negação'
'Para o IS,o valor é comparado com um segundo valor '

ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta, por favor cheque seu e-mail!')


