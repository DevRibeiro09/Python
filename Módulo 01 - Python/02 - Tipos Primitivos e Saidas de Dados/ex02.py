n1 = int (input ('Digite um valor, disgraça:'))
n2 = int (input ('Digite outro:'))
soma = n1 + n2
subtracao = n1 - n2
mult = n1 * n2
div = n1 / n2
print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
print('A diferença entre {} e {} é igual a {}'.format(n1, n2, subtracao))
print('A multiplicação de {} e {} é igual a {}'.format(n1, n2, mult))
print('A divisão entre {} e {} é igual a {}'.format(n1, n2, div))

print(type(soma))