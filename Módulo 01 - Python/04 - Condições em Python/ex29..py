vel = float(input('A que velocidade seu carro estava?'))
multa = (vel - 80) * 7 
if vel > 80:
    print('Você foi multado em R${} reais devido ao excesso de velocidade no trânsito'.format(multa))
else:
    print('Tudo nos conformes. Dirija com cuidado e tenha um bom dia!')