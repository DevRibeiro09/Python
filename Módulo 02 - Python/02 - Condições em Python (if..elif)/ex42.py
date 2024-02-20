# ELABORE UM EXERCÍCIO QUE CALCULE SE 03 SEGMENTOS PODEM OU NÃO FORMAR UM TRIÂNGULO
# SE SIM, DIGA SE O TRIÂNGULO É EQUILÁTERO, ESCALENO OU ISÓSCELES
s1 = float(input('Primeiro Segmento: '))
s2 = float(input('Segundo Segmento: '))
s3 = float(input('Terceiro Segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if s1 == s2 and s2 == s3: # OU s1 == s2 == s3 - O PYTHON PERMITE
        print('Equilátero')
    if s1 != s2 != s3 != s1:  # O PYTHON PERMITE
        print('Escaleno')
    else:                     # SE NÃO FOR NENHUMA DAS OPÇÕES ACIMA, VAI SER ISÓSCELES
        print('Isósceles')
else:
    print('Os segmentos acima não podem formar um triângulo!') # SE NÃO FORMAREM TRIÂNGULO, APARECE ISSO.