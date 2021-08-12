# -*- coding: utf-8 -*-
"""
StringIO

"""
from io import StringIO

mensagem = 'Esta é apenas uma string normal'

#podemos criar um arquivo em memória já com uma string insirida ou mesmo vazio

arquivo = StringIO(mensagem)

print(arquivo.read())

