
"""
Coleções em Python
"""
#Veremos aqui LISTAS:

lista = [1,2,3,4]
print(lista)

lista2 = list(range(11))
print(lista2)


lista3 = list('geek univeristy')
print(lista3)


#Podemos verificar facilmente se um determinado valor está na lista
num = 17
if num in lista2:
    print(f'Encontrei o {num}!')
else:
    print(f'Não encontrei o {num}!')
    
    
#Podemos facilmente ordenar uma lista

lista4 = [27,35,1,58,100,58]
lista4.sort()
print(lista4)

#Podemos contar o número de ocorrências de uma valor em uma lista:

print(lista3.count('e'))

# Para adicionarmos elementos em uma lista:

lista.append(42)
print(lista)
lista.extend([123,5,12])
print(lista)

#Podemos inserir um novo elemento na lista informando a posição do índice:

lista.insert(2,'novo valor')
print(lista)

#Podemos facilmente juntar duas listas

lista5 = lista + lista2
print(lista5)

#Invertendo a lista
lista5.reverse()
print(lista5)

#Podemos facilmente copiar uma lista
lista6 = lista2.copy()
print(lista6)

#Para contar o tamanho de uma lista:
print(len(lista5))

#Podemos remover facilmente o último elemento de uma lista:
#OBS > o pop não só removo o último elemento, mas também o retorna.
lista5.pop()
print(lista5)

#Podemos remover um elemento também pelo índice:

lista5.pop(2)
print(lista5)

#Para removermos todos os elementos de uma lista(limpar):

lista5.clear()
print(lista5)

#Para repetirmos elementos em uma lista:

lista2 = lista2 * 3
print(lista2)

#Transformando uma string em uma lista:

curso = 'Programação em Python'
curso = curso.split()
print(curso)

#Utilizando a vírgula como separador:
curso = 'Programação, em, Python'
curso = curso.split(',')
print(curso)

#Convertendo uma lista em uma string
lista7 = ['Programação', 'em', 'python']
#no comando abaixo é: pegue cada um dos itens da lista e junte colocando
#espaços entre eles
curso =  ' '.join(lista7)
print(curso)


#Iterando sobre listas:

#Exemplo  1 - Utilizando o For.
for elemento in lista:
    print(elemento)
    
#Exemplo 2 - Utilizando o While.

carrinho = []
produto = ''
while produto != 'sair':
    print("adicione um produto na lista ou digite 'sair' ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
        
for produto in carrinho:
    print(produto)
    
#Utilizando váriaveis nas listas

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)
    
#Para gerar índice em um for:
cores = ['azul', 'amarelo', 'vermelho','preto']
for indice, cor in enumerate(cores):
    print(indice,cor)  
    
#Buscando valores através do índice
#Buscando o índice do elemento espeficificado>
print(cores.index('azul'))    
#Buscando o índice do elemento espeficificado a partir de uma posição>
print(cores.index('azul',0))    
#Buscando o índice a partir de uma posição até outra posição>
print(cores.index('azul',0,5))    