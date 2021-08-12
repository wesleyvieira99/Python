# -*- coding: utf-8 -*-
"""
Leitura de arquivos no Python

Para ler o conteúdo de um arquivo em Python, utilizamosa função integrada o
pen(), que literalmente significa ‘abrir’.
Open() -> Na forma mais simples de utilização nós passamos apenas um 
parâmetro de entrada, que neste caso é o caminho para o arquivo a ser lido.
Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

"""
arquivo = open('texto.txt')

print(arquivo.read())

