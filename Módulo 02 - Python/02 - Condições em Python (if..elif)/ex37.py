# FAÇA UM PROGRAMA QUE DÊ 03 OPÇÕES DE CONVERSÃO DE UM NÚMERO
# BINÁRIO, OCTAL E HEXADECIMAL
# AO SELECIONAR, MOSTRAR O VALOR DO NÚMERO CONVERTIDO

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} Convertido para BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} Convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente!')