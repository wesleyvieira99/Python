# -*- coding: utf-8 -*-
"""
Funções com parâmetros padrão

"""

#Função print tem parâmetro opcional, posso ou não informar um param.
print('Geek University!')
print()

#Quando uso parametros padrão, posso ou não colocar parametros iniciais.
def exponencial (numero, potencia=2):
    return numero ** potencia

print(exponencial(3)) #Não passei valor, mas o padrão é dois

#Funções como parâmetro padrão:

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1,num2)

print(mat(2,3))

#Utilizando variável global no escopo local

total = 0

def incremento():
    global total
    
    total = total + 1
    return total

#Usar variável que não é global, somente está no escopo de cima:
    
def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()