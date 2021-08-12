import pickle

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'{self.__nome} está comendo!')

class Gato(Animal):

    def __init__(self, nome):
        self.__nome = nome

    def mia(self):
        print(f'{self._Animal__nome} está miando!')

class Cachorro(Animal):

    def __init__(self, nome):
        self.__nome = nome

    def late(self):
        print(f'{self._Animal__nome} está latindo!')


felix = Gato('Felix')
pluto = Cachorro('Pluto')

#Criando um arquivo com extensão Pickle e escrevendo de forma binária ('wb')
with open('animais.pickle', 'wb') as arquivo:
    #Método dump recebe no primeiro parâmetro o objeto Python e o arquivo para inserir os dados binarizados
    pickle.dump((felix, pluto), arquivo)

#Fazendo a leitura de arquivos de dados Pickle (Trazendo o arquivo binarizado para de volta ao Objeto Python)
with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'o gato chama-se {gato._Animal__nome}')
    gato.mia()
    print(f'o tipo do gato é {type(gato)}')
    print(f'o cachorro chama-se {cachorro._Animal__nome}')
    gato.late()
    print(f'o tipo do gato é {type(cachorro)}')


