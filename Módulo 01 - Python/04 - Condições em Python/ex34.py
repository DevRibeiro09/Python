salario = float(input('Qual seu salário atual? R$ '))
aumento1 = int (salario * 10 / 100)
aumento2 = int (salario * 15 / 100)
if salario > 1250:
    print('Seu salário passará a ser de R${:.2f}'.format(salario + aumento1))
else:
    print('Seu salário passará a ser de R${:.2f}'.format(salario + aumento2))