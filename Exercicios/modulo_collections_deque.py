# -*- coding: utf-8 -*-
"""
Modulo Collections
Deque

"""
#Importar
from collections import deque

#criando deques

deq = deque('geek')

print(deq)



#Adicionando elementos no deque

deq.append('y')

print(deq)

#Adiciona a esquerda com o Deque

deq.appendleft('k')
print(deq)

#Remove a esquerda com o Deque

deq.popleft()
print(deq)