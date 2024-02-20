from datetime import date
def definir_categoria(): #FUNÇÃO
    nome = str(input('Digite seu nome: '))
    anonasc = int(input('Digite seu ano de nascimento: '))
    idade = date.today().year - anonasc
    if idade <= 9:
        print('Sua categoria é Mirim, {}.'.format(nome))
    elif idade > 9 and idade <= 14:
        print('Sua categoria é Infantil, {}.'.format(nome))
    elif idade > 14 and idade <= 19:
        print('Sua categoria é Juvenil, {}.'.format(nome))
    elif idade > 19 and idade <= 25:
        print('Sua categoria é Sênior, {}.'.format(nome))
    elif idade > 25: 
        print('Sua categoria é Master, {}.'.format(nome))
    return()
definir_categoria() #CHAMANDO A FUNÇÃO