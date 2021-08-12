# -*- coding: utf-8 -*-
"""
Preservando Metadatas com Wraps

"""


#Problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma funcao dentro de outra funcao"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b 

print(soma(10, 30))


#Só que ocorre o problema que o name e o doc que vem daqui abaixo tá vindo
#do decorador e não da própria função
print(soma.__name__)
print(soma.__doc__)


