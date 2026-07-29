from datetime import date
sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
if sexo == 'F' :
    print('Você nao precisa se alistar no exercito')
elif sexo == 'M' :
    print('Certo, vamos continuar')
elif idade == 18:
    print('Você deve se alistar imediatamente! ')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alisatado em {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))