# -*- coding: utf-8 -*-
"""
Atributos 

"""
#Construtor em Python
#Atributos de instancia a gente basta declara-los dentro do construtor

#Classes com atributo de instancia públicos
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    
    def __init__(self, conta, limite, saldo):
        self.conta = conta
        self.limite = limite
        self.saldo = saldo
        
        
class Produto:
    def __init__(self, nome, produto, valor):
        self.nome = nome
        self.produto = produto
        self.valor = valor

#Classes com atributo de instancias privadas
class Acesso:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

#Atributos de Classes:
        
class Produto2:
    
    imposto = 1.05
    
    def __init__(self, nome, produto, valor):
        self.nome = nome
        self.produto = produto
        self.valor = (valor * Produto.imposto)



#Atributos Dinâmicos:
        
p1 = Produto('Nika Mercurial', 'Chuteira', 200)
p2 = Produto('Carro', 'Utilitario', 10000)

p2.peso = '5kg' #Note que nao existe na classe Produto

print(p2.peso)