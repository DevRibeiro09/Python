# ESTRUTURA DE REPETIÇÃO 'FOR'
n = int(input('Digite um número: '))
for c in range(0, n+1): #VAI DIGITAR O NÚMERO DE '0' A TAL NÚMERO
    print(c)
print('Final')    

for c in range(0, 3): #FAZ 03 VEZES A PERGUNTA DEVIDO A REPETIÇÃO
    n = int(input('Digite um valor: '))
print('Fim')

s = 0
for c in range(0, 4): #SOMATÓRIO DOS 04 VALORES PEDIDOS NA REPETIÇÃO
    n = int(input('Digite um valor: '))
    s += n
print('A soma de todos os valores foi {}'.format(s))
