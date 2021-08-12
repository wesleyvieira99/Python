# -*- coding: utf-8 -*-
"""
Raise

 A forma geral de utilização é: raise tipoErro(‘Mensagem de Erro’)
"""

raise ValueError('Valor incorreto')

#Caso real

def colore(texto,color):
    if type(texto) is not str:
        raise TypeError('O texto tem que ser string, cabeçao!')
    if type(color) is not str:
        raise TypeError('O texto tem que ser string, cabeçao!')
    print(f'O {texto} será impresso no(a) {color}')

colore('Wes', 'azul') 

colore('Wes', 10)
    