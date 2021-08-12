# -*- coding: utf-8 -*-
"""
Geradores

"""
#Exemplo:

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        #yield é como se fosse o return
        #só que numa funcao normal o return já sai da função
        #só que com funcão geradora retorna e não sai da função, fica 
        #aguardando até uma funcao next() ser chamada novamente
        yield contador
        contador = contador + 1



gen = conta_ate(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for num in gen:
    print(num)
    
gen_lista = list(conta_ate(10))
print(gen_lista)