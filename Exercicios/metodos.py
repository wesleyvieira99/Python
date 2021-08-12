# -*- coding: utf-8 -*-
"""
Métodos em Python

"""

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False
        
class ContaCorrente:
    
    contador = 4999
    
    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:
    
    contador = 0 
    
    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id
        
    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return(self.__valor * (100 - porcentagem))  / 100
        
#Pacote de criptografia SHA 256    
from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    
    contador = 0
    
    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuarios no sistema')
        
    @staticmethod
    def definicao():
        return 'JDJDDIO'
        
    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        #quero encriptar a senha, e estes dois parâmetros significa o quão
        #forte é minha senha
        #rounds é a quantidade de embaralhamento da senha
        #salt é o tamanho do salt da parte do texto que será juntada para
        #criptografar.
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        
    
    #Não é recomendado criar um método personalizado usando dunder
    def __correr__(self, metros):
        print(f' {self.__nome} está corrento {metros} metros!')
       
    #aqui eu checo se minha senha recebida é igual a senha da classe.
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    
    def __gera_usuario(self):
        return self.__email.split('@')[0]
    
user = Usuario('Felicity', 'Jones', 'felcititu@gmail.com', '123456')

Usuario.conta_usuario()
