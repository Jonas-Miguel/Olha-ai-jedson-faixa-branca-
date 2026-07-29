n = int(input('Me fale um numero inteiro qualquer: '))
print('Escolha uma base de converção, \nA:Binario, \nB:octal, \nC:hexadecimal')
escolha = int(input('''Qual das tres opçoes:
[ 1 ] - Binario
[ 2 ] - Octal
[ 3 ] - Hexadecimal
Qual sua escolha? '''))
binario = bin(n)[2:]
octal = oct(n)[2:]
hexadecimal = hex(n)[2:]
if escolha == '1':
    print('A base de converção que você escolheu foi Binario, o numero {} transformado em binario é {}'.format(n,binario))
elif escolha == '2':
    print('A base de converção que você escolheu foi octal, o numero {} transformado em octal é {}'.format(n,octal))
elif escolha == '3':
    print('A base de converção que você escolheu foi hexadecimal, o numero {} transformado em hexadecimal é {}'.format(n,hexadecimal))