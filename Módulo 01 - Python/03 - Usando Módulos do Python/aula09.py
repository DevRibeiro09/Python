# MANIPULANDO CADEIAS DE TEXTO ----------------- 
# '[]' SIGNIFICA LISTA NO PYTHON
# FATIAMENTO - PEGAR PEDAÇOS DE UMA STRING
# LEN = LENGTH (COMPRIMENTO)
# COUNT - CONTAR QUANTAS VEZES APARECE TAL LETRA - EX: frase.count('o')
# REPLACE - REPOSICIONAR UMA PALAVRA POR OUTRA - EX: frase.replace('Python, Android')

# frase.upper() - COLOCAR EM MAIÚSCULAS
# frase.lower() - COLOCAR EM MINÚSCULAS
# frase.captalize() - TODOS OS CARACTERES EM MINÚSCULO, MENOS A PRIMEIRA LETRA DA FRASE
# frase.tittle() - DEIXAR TODAS AS PRIMEIRAS LETRAS DAS PALAVRAS EM MAIÚSCULO
# frase.strip() - REMOVE TODOS OS ESPAÇOS INÚTEIS DA STRING (ESPAÇOS EM BRANCO)

# frase.split() - DIVIDE A STRING EM UMA LISTA - EX: CADA UMA DAS PALAVRAS DA FRASE É PARTE DE UMA LISTA

frase = 'Curso em Vídeo Python'
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print('Oi')
print(frase.capitalize())
print(frase.split())
print("""WELCOME, BABY SHARK
      dsaidasidaj
      daisjdiada
      diosajdisa
      sadas""")