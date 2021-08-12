# -*- coding: utf-8 -*-
"""
Try, Except, Else e Finally

"""



try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto!')
else:
    print(f'Você digitou {num}!')
finally:
    print('Acabou aqui o tratamento de erro!')