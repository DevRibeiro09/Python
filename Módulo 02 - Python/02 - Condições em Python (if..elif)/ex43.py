#CALCULADORA DE IMC
def calculadora_de_imc(): #FUNÇÃO
    peso = float(input('Qual é seu peso (kg)? '))
    altura = float(input('Qual é sua altura (m)? '))
    imc = peso / (altura ** 2) #A ORDEM DOS FATORES NÃO ALTERA O RESULTADO
    print('Seu IMC é de {:.2f}'.format(imc))
    if imc < 18.5:
        print('De acordo com os dados coletados, você está abaixo do peso. Se alimente melhor!')
    elif imc >= 18.5 and imc < 25:
        print('De acordo com os dados coletados, você está no peso ideal!')
    elif imc >= 25 and imc < 30:
        print('De acordo com os dados coletados, você está com sobrepeso. Cuide-se um pouco mais!')
    elif imc >= 30 and imc < 40:
        print('De acordo com os dados coletados, você está obeso. Procure se cuidar!')
    elif imc >= 40:
        print('De acordo com os dados coletados, você está com obesidade mórbida. Procure ajuda médica!')
    return() #NECESSÁRIO PARA RODAR O SCRIPT - PARA DAR O RETORNO DA FUNÇÃO
calculadora_de_imc() #CHAMANDO A FUNÇÃO