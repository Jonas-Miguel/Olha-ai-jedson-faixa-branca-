d = float(input('Qual a distancia da sua viagem? '))
menos = d * 0.50
mais = d * 0.45
if d <= 200 :
    print('Referente essa quilometragem, o valor da sua passagem vai ficar {}'.format(menos))
else:
    print('Referente essa quilometragem, o valor da sua passagem vai ficar {}'.format(mais))