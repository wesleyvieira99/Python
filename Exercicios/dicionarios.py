# -*- coding: utf-8 -*-
"""
Dicionários ---

São coleções do tipo chave/valor
Dicionário são representados no Python por chaves {}
"""

#Forma 1
paises = {'br': 'Brasil', 'eua': 'Estados Unidos'}

print(paises)

#Forma 2 (Menos Comum)

paises = dict(br='Brasil', eua='Estados Unidos')

print(paises)

# Acessando elementos

#Forma 1 - Acessando via chave, da mesma forma que lista/tupla.

print(paises['br'])
print(paises['eua'])

#Forma 2 - Acessando via get (forma recomendada)

print(paises.get('br'))
print(paises.get('eua'))

#Dentro desta forma usando o get podemos até colocar um valor padrão
#caso o valor não exista ou não seja encontrado
pais = paises.get('ru', 'Não encontrado')
print(pais)

#Podemos identificar se algum item está contido dentro do dicionário:
print('br' in paises)

if 'br' in paises:
    print('encontrei')
else: 
    print('não encontrei')
    

#Podemos utilizar qualquer tipo de dado (int, float, string, boolean, etc)
#inclusive lista, tulpa, dicionário, como chaves de dicionários
    
localidades = {
    (35.6895, 39.6917): 'Escritório em Nova York',
    (35.6565, 39.6187): 'Escritório em São Paulo',
    (35.7458, 39.6267): 'Escritório em Dublin',    
}

print(localidades)

#Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

#Forma 1 de adicionar:

receita['abr'] = 350
print(receita)

# Forma 2 de adicionar:

novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# Atualizando dados já existentes:

#Forma 1

receita['mai'] = 500
print(receita)

#Forma 2 
receita.update({'mai': 600})
print(receita)

#Removendo dados de um dicionário:

#Forma 1 - mais comum:
#Para remover é obrigatório sempre informar a chave pra excluir
#E caso não encontre o elemento um KeyError é retornado.
receita.pop('mar')
print(receita)

#Forma 2:

del receita['fev']
print(receita)

"""
Vamos entender onde usaria um dicionário: 
    Imaginamos que temos um comércio eletrônico no qual
    temos um carrinho de compras onde inserimos produtos e
    preços, o dicionário ajuda justamente nisto. Para armazenar
    estas informações poderíamos usar uma lista também.

"""
# Comercio eletronico com lista - Carrinho
carrinho = []
prod1 = ['PlayStation', 1, 2300]
prod2 = ['God Of War', 1, 150]
    
carrinho.append(prod1)
carrinho.append(prod2)
print(carrinho)

#Teríamos que saber qual é o índice de cada informação no produto.
#Com dicionários resolveríamos isso, ao invés de utilizarmos dicionários:

carrinho = []

prod1 = {'nome': 'PlayStation 4', 'qtd': 1, 'preço': 2300}
prod2 = {'nome': 'God of War', 'qtd': 1, 'preço': 150}

carrinho.append(prod1)
carrinho.append(prod2)

print(carrinho)

#Utilizando dicionários temos as informações bem mais definidas do que
#Utilizando tuplas ou listas. Com dicionários podemos ter a certeza
#sobre cada informação.


# Métodos de dicionários:

d = dict(a=1, b=2, c=3)
print(d)

#1. Limpar o dicionário:

d.clear()
print(d)

#2. Copiando um dicionário para outro:

#Forma 1 - Deep Copy
novo = d.copy()
print(novo)
#Forma 2 - Shallow Copy
novo = d
print(novo)


#Forma não usual de criação de dicionários:
outro = {}.fromkeys('a','b')
#Cria uma chave 'a' com valor 'b'
print(outro)

usuario = {}.fromkeys(['nome','pontos','email'], 'desconhecido')
print(usuario)
