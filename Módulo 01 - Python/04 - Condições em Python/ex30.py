numero = int(input('Digite um número: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é par'.format(numero))
else:   
    print('O número {} é impar'.format(numero))
    
# A SOBRA DA % É QUE DA O RESULTADO SE É IMPAR OU PAR, DEVIDO A SOBRA DA DIVISÃO POR 2
# 5 DIVIDIDO POR 2 = 1 DE SOBRA, OU SEJA, É IMPAR
# 2 DIVIDIDO POR 2 = 0 DE SOBRA, OU SEJA, É PAR