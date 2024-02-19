salario = float(input('Qual o salário do seu funcionário? R$'))
novosalario = salario + (salario * 15 / 100 )
print('Houve um aumento de 15% do salário.')
print('De acordo com o rejuste salarial, com um aumento de 15% seu novo salário será de R${:.2f}'.format(novosalario))

