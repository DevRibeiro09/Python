# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACOROD COM SUA IDADE:
# SE ELE AINDA VAI SE ALISTAR, SE JÁ ESTÁ NA HORA OU SE JÁ PASSOU DO TEMPO DE ALISTAMENTO;
# O PROGRAMA DEVE MOSTRAR TAMBÉM O TEMPO QUE FALTA/PASSOU DO PRAZO.
from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar imediatamente!!')
elif idade < 18:
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para se alistar.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(atual + (18 - idade)))
elif idade > 18: #ELIF E ELSE DÁ CERTO NO ÚLTIMO CASO
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('O ano de seu alistamento foi em {}.'.format(atual - (idade - 18)))
