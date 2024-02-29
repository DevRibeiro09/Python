#PROGRAMA QUE LEIA 06 NÚMEROS E SOME APENAS OS PARES
#SE O VALOR DIGITADO FOR IMPAR, DESCONSIDERAR
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0: #IGNORA OS NÚMEROS IMPARES E SÓ SOMA OS PARES
        soma += num
        cont += 1
    else:
        print('Número Ímpar - Inválido') #ANULA O NÚMERO IMPAR DA SOMA
print('Você informou {} números e a soma foi {}'.format(cont, soma))
