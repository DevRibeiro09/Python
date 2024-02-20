def calcular_media(): #FUNÇÃO
    nota1 = float(input('Primeira Nota: '))
    nota2 = float(input('Segunda Nota: '))
    nota3 = float(input('Terceira Nota: '))
    nota4 = float(input('Quarta Nota: '))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media < 5:
        print('Sua média foi {}.'.format(media))
        print('Reprovado. Estude mais!')
    elif media > 5 and media < 7:
        print('Sua média foi {}.'.format(media))
        print('Recuperação. Tem uma nova chance!')
    elif media >= 7:
        print('Sua média foi {}.'.format(media))
        print('Aprovado!')   
calcular_media() #CHAMANDO A FUNÇÃO 
                 #SE NÃO CHAMAR A FUNÇÃO, O SCRIPT NÃO RODA

