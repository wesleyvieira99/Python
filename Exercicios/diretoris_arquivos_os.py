# -*- coding: utf-8 -*-
"""
Sistema de Arquivos - Manipulação

"""
import os

#Descobrindo se um arqivo ou diretório exite
print(os.path.exists('arquivo.txt'))

#Somente criando arquivos - Forma 1
open('arquivo-teste.txt', 'w').close()

#Somente criando arquivos - Forma Correta
with open('arquivo-teste.txt', 'w') as arquivo:
    pass

#Somente criando arquivos - segunda maneira correta
os.mknod('arquivo.txt')

#Criar um diretório

os.mkdir('templates')

#Criando uma árvore de diretórios

os.makedirs('templates/geek/university')

#Renomear arquivos e diretórios

os.rename('templates2', 'geek2')
os.rename('geek2/novo2/outro2/teste.txt', 'geek2/novo2/outro2/geek.txt')

#Remover um arquivo
os.remove('geek.txt')


#Pegar o current directory
print(os.getcwd())

#Para mudar o diretório atual para outro
os.chdir('..')

#Identificar o meu sistema operacional
print(os.name())

#juntar meu diretório atual a outro
os.path.join(os.getcwd(), 'geek')

#listar os arquivos e diretórios
print(os.listdir())

#removendo diretórios vazios
os.rmdir('templates')

#removendo uma árvore de diretorios
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)

#removendo uma árvore de diretórios vazios
os.removedirs('geek2/outro/mais')

#remover arquivos para lixeira, podendo restaura-los
from send2trash import send2trash

send2trash('cesta2.txt')

#Trabalhando com arquivos e diretórios temporários
#Cria um diretório na minha maquina temporariamente
#Utilizo o input pra segurar esse diretorio temporario
#Quando dou enter e saiu do input, o diretorio temporario se apaga
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arq:
        arq.write('Geek University')
    input()
    
#Agora criando um arquivo temporário
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University')
    #Esse 'b' converte essa string para binário, ou seja, bits (0 e 1)
    #Isso por que a gente só consegue escrever dados binários nesse 
    #arquivo temporário.
            







