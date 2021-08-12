"""
Lendo Arquivos CSV - Comma Separated Values - Valores separados por vígular


with open('mutators.csv') as archive:
    dados = archive.read()
    dados = dados.split(',')
    print(dados)

"""

#Reader - Trabalhar com CSV como listas

from csv import reader
with open('mutators.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) #Pular uma linha do CSV, serve para pular o cabeçalho
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]} cm.')
#Como temos uma lista para trabalhar, cada linha do arquivo é uma lista para trabalharmos.

#DictReader - Trabalhar CSV como dicionário:

from csv import DictReader

with open('mutators.csv') as arq:
    leitor_csv = DictReader(arq)
    for linha in leitor_csv:
        #Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu em {linha['Pais']} e tem {linha['Altura']}")
        #Não precisamos dar next pois o cabecalho ja é entendido como chave
        #Devemos usar aqui os parâmetros com o mesmo nome das chaves do CSV
