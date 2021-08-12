# -*- coding: utf-8 -*-
"""
Seek e Cursors

"""


arquivo = open('texto.txt')

print(arquivo.read())

#Movimentando o cursor pelo arquivo com a função seek

arquivo.seek(5)
#movimentei meu cursor para o ponto 5 no texto
print(arquivo.read())

#  usar três vezes o readline para imprimir as três primeiras linhas
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

#readlines e len em conjunto

linhas = arquivo.readlines()

print(len(linhas))

arquivo.close()

