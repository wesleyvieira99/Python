from csv import writer

#Criando um arquivo 'filmes.csv'
with open('filmes.csv', 'w') as arq:
    #abrindo o escritor csv
    escritor_csv = writer(arq)
    #variavel inicializada com None
    filme = None
    #escrever meu cabecalho - o método writerow utiliza lista para escrever a linha
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])
