# -*- coding: utf-8 -*-
"""
Bloco With
O bloco With é utilizado para criar um contexto de trabalho com os 
arquivos que manipulamos, onde os recursos utilizados são fechados após 
o bloco With.

"""

with open('texto.txt') as arquivo:
    print(arquivo.readlines())


