alt = float(input('Qual a altura da parede? '))
larg = float(input('Qual a largura da parede?'))
area = alt * larg
tinta = area / 2
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².'.format(alt, larg, area))
print('Para pintar essa parede você precisará de {:.2f}l de tinta'.format(tinta))