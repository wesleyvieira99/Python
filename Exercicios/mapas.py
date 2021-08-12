# -*- coding: utf-8 -*-
"""
Mapas - Conhecidos em Python como DICIONÁRIOS
"""

receita = {'jan': 100, 'fev': 250}

print(receita)

#Iterar sobre dicionários
for chave in receita:
    print(chave)
    
for chave in receita:
    print(receita[chave])
    
for chave in receita:
    print(f'{chave} : {receita[chave]}')

#Para trazer todas as minhas chaves do dicionário:

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])
    
#Acessando os valores
    
print(receita.values())

for valor in receita.values():
    print(valor)
    
#Desempacotamento de dicionários:

for chave, valor in receita.items():
    print(chave, valor)
    
#Soma, valor max, valor min e tamanho posso usar também, conforme listas e tuplas

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
