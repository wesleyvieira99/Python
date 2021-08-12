# -*- coding: utf-8 -*-
"""
Conjuntos em Python...

Os conjuntos no Python são chamados de Sets
Estes Sets (Ou conjuntos) não possuem valores duplicados, 
valores ordenados e elementos não são acessados via índice, 
ou seja, conjuntos não são indexados ...
Conjuntos são bons para se utilizar quando precisamos 
armazenar elementos mas não nos importamos com a ordenação deles, 
quando não precisamos se preocupar com chaves, valores itens duplicados...
Os conjuntos ou Sets, são referenciados em Python chaves {} 
também como os mapas...
Os conjuntos ou Sets, são referenciados em Python chaves {} 
também como os mapas...
Mas há diferenças entre conjuntos (sets) e mapas (dicionários em Python:
•	Um dicionário tem chave e valor;
•	Um conjunto só tem valor, apenas isso;

"""


#Definindo um conjunto

#Forma 1

s = set({1,2,3,4,5,5,6,7,2,3}) #Repare que temos valores repetidos e não ordenados

print(s)
#Caso haja algum valor já existente, o mesmo será ignorado e não fará parte do conjunto.

#Forma 2 - Mais comum

s = {1,2,3,4,5,6,5}
print(s)

#Conseguimos também converter listas, tuplas e strings para um set:

s = set('Oi, tudo bem?')

lista = [1,2,3,4,5,5]
set(lista)

#Verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')
    
#Importante lembrar que além de não termos valores duplicados, não temos ordem:

s = {99,2,23,5,1,1,88,1000}
print(s)

#Vale sempre a pena lembrar:
#Listas aceitam valores duplicados;
#Tuplas também aceitam valores duplicados;
#Dicionários não aceitam chaves duplicadas;
#Conjuntos não aceitam valores duplicados.

#Assim como todo outro conjunto Python, podemos colocar todos os tipos d
#e dados misturados em Sets...

s = {1, 'b', True, 34.50}
print(s)

#•	Imagine que fizemos um sistema de cadastro de uma feira ou museu e os 
#visitantes informaram manualmente cidade de onde vieram. Nós adicionamos cada
# cidade em uma lista Python, já que em uma lista podemos adicionar novos
# elementos e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'São Paulo', 'Campo Grande']
print(cidades)
print(len(cidades))
#•	Só que agora precisamos saber quantas cidades distintas, ou seja, únicas temos:

s = set(cidades)
print(s)
print(len(s))

#Adicionando elementos em um conjunto
#Conjuntos são mutáveis
s = {1,2,3}
s.add(4)
print(s)

#Removendo elementos em um conjunto

s.remove(2)
print(s)

#Copiando um conjunto para outro:

#Forma 1 - Deep Copy

novo = s.copy()
print(novo)
novo.add(5)
print(novo)

#Forma 2 - Shallow Copy

novo = s
novo.add(5)
print(novo)
print(s)

#Removendo todos os elementos de um conjunto:

s.clear()
print(s)

#Métodos matemáticos de conjuntos:

#•	Imagine que temos dois conjuntos, um com estudantes de Python e outro de JAVA:

python = {'marcos', 'julia', 'wes'}
java = {'Fernando', 'gustavo', 'julia' }

#Veja que a julia estuda python e java, está nos dois conjuntos...
#Precisamos gerar um conjunto com nomes de estudantes únicos

#Forma 1- Utilizando union

unicos1 = python.union(java)
print(unicos1)

#Forma 2 - utilizando o caractere pipe "|":

unicos2 = python | java
print(unicos2)

#Intersecção entre os dois conjuntos:

#Forma 1
ambos1 = python.intersection(java)
print(ambos1)

#Forma 2
ambos2 = python & java
print(ambos2)

#Estudantes que estão onos cursos não estão no outro

so_python = python.difference(java)
print(so_python)

so_java = java.difference(python)
print(so_java)


