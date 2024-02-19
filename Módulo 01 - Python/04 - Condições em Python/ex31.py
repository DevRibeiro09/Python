distancia = float(input('Qual a distância da sua viagem? '))
resultado1 = distancia * 0.50
resultado2 = distancia * 0.45
print('Você está prestes a começar uma viagem de {:.1f}km'.format(distancia))
if distancia <= 200:
    print('Sua viagem custará R${:.2f}'.format(resultado1))
else: 
    print('Sua viagem custará R${:.2f}'.format(resultado2))