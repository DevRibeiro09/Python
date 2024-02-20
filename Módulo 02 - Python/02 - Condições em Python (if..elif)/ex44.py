#GERENCIADOR DE PAGAMENTOS
# A VISTA: DINHEIRO OU PIX - 1O% DESCONTO
# A VISTA NO CARTÃO - 5% DESCONTO
# EM ATÉ 2X NO CARTÃO - PREÇO NORMAL
# 3X OU MAIS NO CARTÃO - 20% JUROS
print('{:=^40}'.format(' ATACADÃO RIBEIRO '))
compra = float(input('Qual o valor total da compra? R$'))
total = compra
parcela = (total / 2)
print('''FORMAS DE PAGAMENTO
    [1] À VISTA - DINHEIRO OU PIX
    [2] À VISTA - 1X NO CARTÃO
    [3] 2X NO CARTÃO (SEM JUROS)
    [4] 3X OU MAIS NO CARTÃO (COM JUROS)''')
opçao = int(input('Qual a forma de pagamento? '))
if opçao == 1:
    total = compra - (compra * 10 / 100)
    print('Sua compra de R${:.2f} passará a ser de R${}.'.format(compra, total))
elif opçao == 2:
    total = compra - (compra * 5 / 100)
    print('Sua compra de R${:.2f} passará a ser de R${}.'.format(compra, total))
elif opçao == 3:
    total = compra
    parcela = (total / 2)
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opçao == 4:
    parcelamento = int(input('Em quantas vezes quer dividir? '))
    total = compra + (compra * 20 / 100)
    parcelas = total / parcelamento
    print('Sua compra de R$ {} será dividida em {}X de R${}'.format(compra, parcelamento, parcelas))
else:
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE')

print('{:=^40}'.format(' ATACADÃO RIBEIRO '))
print('{:=^40}'.format('AGRADEÇEMOS A PREFERÊNCIA'))
