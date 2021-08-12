# -*- coding: utf-8 -*-
"""
Funções decoradoras com diferentes parâmetros de entrada...
Com assinaturas diferentes
Utilizamos o decorator pattern, *args e **kwargs
"""
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}!'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}!'

#Testando
    
print(saudacao('Wesley'))
print(ordenar('Arroz', 'Suco'))

#Decorator com parâmetro de entrada

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorret! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)
    
print(comida_favorita('arroz'))
print(comida_favorita('pizza'))