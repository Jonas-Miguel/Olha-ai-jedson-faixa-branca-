ano = int(input('Digite um ano para saber se ele é bissexto: '))
if ano % 4 == 0 :
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} NÃO é um ano bissexto'.format(ano))