peso = float(input('Qual o peso? (kg) '))
altura = float(input('Qual a altura? (m) '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('O IMC dessa pessoa testa em {:.1f}, esta abaixo do peso!'.format(imc))
elif (imc >= 18.6) and (imc <= 25):
    print('PARABÉNS, o seu IMC esta em {:.1f}, voce esta no peso ideal!'.format(imc))
elif (imc >= 25.1) and (imc <= 30):
    print('Entao o sei IMC esta em {:.1f}, Voce esta sobrepeso!'.format(imc))
elif (imc >= 30.1) and (imc <= 40):
    print('Rapaz os eu IMC esta em {:.1f} e voce esta obeso!'.format(imc))
elif imc >= 40.1:
    print('Você esta com o imc de {:.1f}, voce esta com obesidade morbida'.format(imc))
