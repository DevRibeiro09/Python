# .strip ELIMINA ESPAÇOS EM BRANCO ANTES E DEPOIS
# -nome.count(' ') REMOVE O ESPAÇO EM BRANCO ENTRE AS PALAVRAS

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} caracteres'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))