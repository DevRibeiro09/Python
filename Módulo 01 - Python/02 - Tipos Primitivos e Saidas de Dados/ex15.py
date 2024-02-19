dias = int(input('Por quantos dias alugastes o carro? '))
km = float(input('Quantos KM rodou? '))
aluguel = (60 * dias) + (0.15 * km)
print('Total a pagar: R${:.2f}'.format(aluguel))