# ESCREVA UM PROGRAMA PARA APROVAR UM EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA.
# PERGUNTE O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE PRETENDE PAGAR.
# A PRESTAÇÃO MENSAL NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO.

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = (salario * 30 / 100)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, prestação))
if prestação <= minimo:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')
