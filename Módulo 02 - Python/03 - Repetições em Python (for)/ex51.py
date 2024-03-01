#PROGRESSÃO ARITMÉTICA
num = int(input('Digite um número: '))
razao = int(input('Razão: '))
decimo = num + (10 - 1) * razao
for p in range(num, decimo + razao, razao):
    print('{}'.format(p))
print('FIM')
