#TABUADA DE UM NÚMERO LIDO NO INPUT
from time import sleep
num = int(input('Digite um número: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
    sleep(0.5)
print('TABUADA DO NÚMERO {}'.format(num))    
print('FINAL')
