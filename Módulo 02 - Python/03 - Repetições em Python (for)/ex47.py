#PROGRAMA QUE MOSTRE TODOS OS NÚMEROS PARES ENTRE 01 E 50
for cont in range(0, 51, 2): #CONTAGEM DE 02 EM 02 DEVIDO AO TERCEIRO TERMO
    print(cont)
print('Final')

num = int(input('Digite um número: ')) #O PROGRAMA MOSTROU OS NÚMEROS PARES DE '0' A 'X'
for c in range(0, num+1, 2): #O 'NUM+1' DEFINIU O ÚLTIMO NÚMERO JUNTO DOS OUTROS, SEM ELE SÓ MOSTRA ATÉ O PENÚLTIMO NÚMERO PAR
    print(c)
print('Acabou')

