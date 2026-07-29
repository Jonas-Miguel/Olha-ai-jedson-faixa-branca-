nome = input('Qual o seu nome?')
data = input('olá {},qual a seu ano de nascimento? '.format(nome))
ano_atual = int(input('Qual o ano atual? '))
ano_alistamento = data + 18
if ano_atual >= ano_alistamento:
    