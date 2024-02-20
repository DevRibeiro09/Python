# JO KEN PO - PEDRA, PAPEL E TESOURA
def jokenpo():
    from random import randint
    from time import sleep
    nome = str(input('Qual seu nome? '))
    print('Bem-vindo(a), {}! Vamos jogar?'.format(nome))
    itens = ('Pedra','Papel','Tesoura')
    computador = randint(0,2)
    print('''Suas opções:
        [0] Pedra
        [1] Papel
        [2] Tesoura''')
    jogador = int(input('Qual é a sua jogada?'))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    print('-='*10)
    print('Computador jogou {}'.format(itens[computador]))
    print('{} jogou {}'.format(nome, itens[jogador]))
    print('-='*10)
    if computador == 0: #PEDRA
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('{} VENCEU'.format(nome))
        elif jogador == 2:
            print('COMPUTADOR VENCEU')
        else:
            print('Jogada Inválida!')
            
    elif computador == 1: #PAPEL
        if jogador == 0:
            print('COMPUTADOR VENCEU')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('{} VENCEU'.format(nome))
        else:
            print('Jogada Inválida!')
            
    elif computador == 2: #TESOURA
        if jogador == 0:
            print('{} VENCEU'.format(nome))
        elif jogador == 1:
            print('COMPUTADOR VENCEU')
        elif jogador == 2:
            print('EMPATE')
        else:
            print('Jogada Inválida!')
    return()
jokenpo()