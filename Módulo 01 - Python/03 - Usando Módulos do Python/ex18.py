import math
ang = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(ang))
print('O ângulo {:.2f} tem o SENO de {:.2f}'.format(ang, seno))
cosseno = math.cos(math.radians(ang))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(ang, cosseno))
tangente = math.tan(math.radians(ang))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(ang, tangente))