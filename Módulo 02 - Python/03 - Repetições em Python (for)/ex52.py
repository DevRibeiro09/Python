#DETERMINAR SE UM NÚMERO É PRIMO E POR QUANTOS NÚMEROS ELE É DIVISÍVEL
num = int(input('Digite um número: '))
divisiveis = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='') #AMARELO SE FOR DIVISÍVEL
        divisiveis += 1
    else:
        print('\033[31m', end='') #VERMELHO SE NÃO FOR DIVISÍVEL
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, divisiveis))
if divisiveis == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO é PRIMO')
