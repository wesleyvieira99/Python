# -*- coding: utf-8 -*-
"""
Entendendo os *kargs

Ele força que utilizemos parâmetros nomeados e transforma esses parâmetros 
extras em um dicionário.
"""

def cores(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'a cor favorita de {pessoa} é {cor}')

cores(marcos='verde', fernanda='amarelo')

#Desempacotando usando o **kwargs:

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"
#Retorna o valor do kwargs das chaves nome e sobrenome
    
nomes = {'nome': 'Wesley', 'sobrenome': 'Vieira'}

print(mostra_nomes(**nomes))

#Outro exemplo:

def soma_multiplos_numeros(a,b,c):
    print(a+b+c)
    
dicionario = dict(a=1,b=2,c=3)
soma_multiplos_numeros(**dicionario)

#Os nome das chaves em um dicionário devem ser os mesmos dos parâmetros da 
#função.