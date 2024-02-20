# CONDIÇÕES ANINHADAS

# IF
# ELIF (ELSE + IF)
# ELSE 

# PODE-SE UTILIZAR O 'ELIF' QUANTAS VEZES FOREM NECESSÁRIAS
# 'ELSE' APENAS UMA OU NENHUMA VEZ
# NUNCA PODE USAR 'ELIF' SEM 'IF'

nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':   #CONDIÇÃO SIMPLES
    print('Que nome bonito.')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Samuel' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica, Juliana':
    print('Belo nome feminino')
print('Tenha um bom dia, {}!'.format(nome))
