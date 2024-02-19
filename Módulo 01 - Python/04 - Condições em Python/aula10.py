print('---------CALCULADOR DE MÉDIA ANUAL----------')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
m = (n1 + n2 + n3 + n4)/4
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Você passou, parabéns!')
else:
    print ('Você foi reprovado, estude mais!')