#FAÇA UM PROGRAMA QUE MOSTRE SE UM NÚMERO É MAIOR, MENOR OU IGUAL A OUTRO

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if n1 > n2:
    print('O número {:.1f} é maior que o número {:.1f}.'.format(n1, n2))
elif n1 == n2:
    print('Não há número maior, os dois são iguais!')
else:
    print('O número {:.1f} é maior que o número {:.1f}.'.format(n2, n1))


    