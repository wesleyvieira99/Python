# -*- coding: utf-8 -*-
"""
Entendo *args

Ele é um parâmetro de entrada de uma função como outro qualquer, eu
posso chamá-lo de qualquer coisa, desde que comece com asterisco.
Mas, por convenção, foi adotado o nome args, ficando *args.
,O parâmetro *args é utilizado em função, coloca os valores extras
informados como entrada em uma tupla, então desde já lembre-se que
tuplas são imutáveis.
"""

#Exemplos sem o *args:

def soma_tudo(num1=1, num2=2,num3=3):
    return num1 + num2 + num3


#Exemplos com o *args:

def soma_tudo_args(*args):
    return sum(args)

print(soma_tudo_args(10,20))
print(soma_tudo_args(10,20,20,30))
    

#Outro exemplo de utilização do args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek!'
    return 'Eu não sei quem é você!'

print(verifica_info())
print(verifica_info(True))
print(verifica_info(1, 2))
print(verifica_info('Geek', 'University'))
    
#Desempacotando valores de uma coleção para usar no *args:

numeros = [1,2,3,4,5,6]

numeros2 = {1,2,3,4,5,6}

print(soma_tudo_args(*numeros))
print(soma_tudo_args(*numeros2))






