# -*- coding: utf-8 -*-
"""
Decoradores

"""


#Decoradores como funções - Sintaxe não recomendada, sem a "@"

#Decorador, estamos decorando a função 'saudacao'
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia')
    return sendo

def saudacao():
    print('Seja bem-vindo à Geek University!')
    
#Testando 01
    
teste = seja_educado(saudacao)

teste()


#Decoradores como funções - Sintaxe recomendada, com a "@"

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

#Testando - Simplesmente executamos a função:
apresentando()

