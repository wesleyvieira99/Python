# -*- coding: utf-8 -*-
"""
Criando nossa própria versão de Loops

"""
for num in [1,2,3,4,5]:
    print(num)
    
for letra in ' Geek University':
    print(letra)
    
    
#Minha versão do loop
    
def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('geek university')