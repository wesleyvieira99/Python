# -*- coding: utf-8 -*-
"""
Abstração e Encapsulamento

"""

class Conta:
    contador = 400
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
        
    def extrato(self):
        print(f'Saldo de {self.__saldo} do titualr {self.__titular} com limite de {self.__limite}')
        
    def depositar(self, valor):
        self.__saldo += valor
        
    def sacar(self, valor):
        self.__saldo -= valor

#Testando

conta1 = Conta('Geek', 1500, 2000)

print(conta1)

print(conta1._Conta__titular)
print(conta1._Conta__saldo)
print(conta1._Conta__limite)
print(conta1._Conta__numero)

conta2 = Conta('Wes', 5000, 10000)

print(conta2)

print(conta2._Conta__titular)
print(conta2._Conta__saldo)
print(conta2._Conta__limite)
print(conta2._Conta__numero)

conta1.extrato()
conta2.extrato()



