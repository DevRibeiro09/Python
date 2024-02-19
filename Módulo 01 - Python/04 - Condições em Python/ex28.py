from random import randint
from time import sleep #WAIT 2SEC 
computador = randint(0,5) #FAZ O COMPUTADOR PENSAR NO NÚMERO
print('_' * 10)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('_' * 10)
jogador = input('Em que número eu pensei? ') #JOGADOR TENTA ADIVINHAR
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Você ganhou!')
else: 
    print('Você perdeu!')
