"""
#Um dado é considerado sempre do tipo string sempre que estiver:
#Entre aspas simples;
#Entre aspas duplas;
#Entre aspas simples triplas;
#Entre aspas duplas triplas;

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \n Jolie'
print(nome)
print(type(nome))

#o \n acima serve para pular uma linha em uma string
print(nome.lower())
nome = 'Geek, University'
print(nome.split(','))

#split acima transforma em uma lista de strings

"""

nome = 'Geek University'
print(nome[0:4])

#o comando acima pega a primeira letra até a 3, pois não inclui o 4.

print(nome[5:15])
#o que estamos fazendo aqui acima se chama slice de strings.

#abaixo digo para ir até o ultimo elemento a partir do primeiro elemento
print(nome[::])

#faço o mesmo de cima porém agora eu inverto a palavra
print(nome[::-1])

#abaixo eu substituo nesta string as letras G por P.
print(nome.replace('G','P'))