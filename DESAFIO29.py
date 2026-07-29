v = int(input('Qual a velocidade do carro? '))
m = (v - 80) * 7
if v > 80:
    print('O cidadão você esta acima da velocidade permitida, e ira pagar 7.00 por km acima da velocidade, o valor da \nsua multa ficou {}'.format(m))