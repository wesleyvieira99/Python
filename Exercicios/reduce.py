# -*- coding: utf-8 -*-
"""
REDUCE

Para entendermos o reduce, imagine que temos uma coleção de dados e você tem uma função que recebe dois parâmetros (função(x,y)) e retorna um valor. Assim como map e filter, a reduce recebe dois parâmetros: função e dados.
Com isso, a função reduce() funciona da seguinte maneira: 
1.	Res1 = função(dado1, dado2) -> aplica a função nos dois primeiros elementos da coleção e guarda o resultado;
2.	Res2 = função(res1, dado3) -> resultado do calculo anterior e o próximo dado como parâmetros
Esses passos são repetidos até o final da coleção, assim por diante, sempre pegando o resultado anterior.
EM CADA PASSO ELA APLICA A FUNÇÃO PASSANDO COMO PRIMEIRO ARGUMENTO O RESULTADO DA APLICAÇÃO ANTERIOR, NO FINAL REDUZ E IRÁ RETORNAR O RESULTADO FINAL.


"""

from functools import reduce
dados = [1,2,3,4,5,6,7,8,9,10]

print(reduce(lambda x,y: x * y,dados))