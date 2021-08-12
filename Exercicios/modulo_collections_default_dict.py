# -*- coding: utf-8 -*-
"""
Módulo Collections
Default Dict

"""


#Criação e uso de dicionários como já conhecemos...
dicionario = {'curso': 'Programação'}

print(dicionario)

print(dicionario['curso'])

#Colocando um dicionário default para o meu dicionário
#Ou seja, já inicializado com esta forma.
#O Default Dict não apresenta Key Erro.
#Ao criar um dicionário utilizando-o nós informamos um valor Default
#Podendo utilizar um Lambda para isso, esete valor será utilizado
#Sempre que não houver um valor definido
#Caso tentemos acessar uma chave que não existe, essa chave será criada
#E o valor default será atribuído a essa nova chave criada:

#OBS: Lambdas são funções sem nome que podem ou não receber parâmetros 
#De entrada e retornar valores

from collections import defaultdict

dicionario = defaultdict(lambda: 0)
#variável dicionario recebendo o defaultdict com uma função lambda que retorna 0

dicionario['curso'] =  'Programação'
print(dicionario)

print(dicionario['outro'])
print(dicionario)


