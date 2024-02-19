# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACOROD COM SUA IDADE:
# SE ELE AINDA VAI SE ALISTAR, SE JÁ ESTÁ NA HORA OU SE JÁ PASSOU DO TEMPO DE ALISTAMENTO;
# O PROGRAMA DEVE MOSTRAR TAMBÉM O TEMPO QUE FALTA/PASSOU DO PRAZO.
from datetime import date
anonasc = int(input('Em que ano você nasceu? '))
dataatual = date.today()
idade = dataatual - anonasc
if idade < 18:
    print('Você ainda não tem idade para se alistar no exército!')
    print('Ainda faltam {} anos para se alistar'.format())
elif idade > 18:
    print('Você já passou do tempo de se alistar, sua disgraça!')
    print('Passou {} anos do prazo. Vai levar multa pra ficar esperto!'.format())
else: 
    print('Você deve se alistar imediatamente!')
    print('Já alcançou a idade necessária.')
