from datetime import date
atual = date.today().year
atleta = str(input('Qual o nome do atleta: ')).title()
nasc = int(input('Qual o ano do nascimento {} ? '.format(atleta)))
idade = atual - nasc
if idade <= 9:
    print('Olá {}, você tem {} anos, voce é um atleta Mirim'.format(atleta,idade))
elif 9 < idade <= 14:
    print('Olá {}, você tem {} anos, voce é um atleta infantil'.format(atleta,idade))
elif 14 < idade <= 19:
    print('Olá {}, Voce tem {} anos, você é im atleta junior'.format(atleta,idade))
elif 19 < idade <= 25:
    print('Ola {}, você tem {}anos , voce é um atleta senior'.format(atleta,idade))
elif idade > 25:
    print('Olá {}, Você tem {} anos você é um atleta master'.format(atleta,idade) )