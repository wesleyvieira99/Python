# -*- coding: utf-8 -*-
"""
Escrevendo em arquivos

"""


with open('texto.txt','w') as arquivo:
    arquivo.write('\n Escrever dados em arquivos é muito fácil caraio. \n')
    arquivo.write('Esta é a ultima linha porra!!!! \n')
    
    # \n significa Enter, pular uma linha

with open ('texto.txt') as arquivo:
    print(arquivo.read())
    
    
with open('frutas.txt', 'w') as arq:
    while True:
        fruta = input('Digite uma fruta:')
        if fruta!= 'sair':
            arq.write(fruta + '\n')
        else:
            break