# -*- coding: utf-8 -*-
"""
Iterador Customizável

"""

class Contador:
    #método inicializador, ou seja, construtor (__init__)
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior
    
    #método para transformar minha classe num interável
    def __iter__(self):
        return self
    
    #método para iterar
    #se o meu parametro menor for menor que o meu parametro maior
    #eu coloco na minha variável numero o valor de menor
    #incremento mais um no meu parametro menor
    #por conta do next, vou realizando o loop
    #saio do loop (raise) caso houve o StopIteration
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration
        
        
con = Contador(1, 61)

#acessar o primeiro atributo
print(con.menor)

#acessar o segundo atributo
print(con.maior)

#transformar minha classe com meu método num interável

it = iter(con)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

for n in Contador(1,50):
    print(n)