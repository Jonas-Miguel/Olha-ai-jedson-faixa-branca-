from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)
print(''' Vamos Jogar JO KEN PO
Essas são suas opções : '
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual sua jogada : '))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' *15)
print('Jogador jogou {}'.format(itens[jogador]))
print('Computador jogou {}'.format(itens[computador]))
print('-=' *15)
if computador == 0: #pedra
    if jogador == 0:
        print('EMPATE!!!')
    elif jogador == 1:
        print('JOGADOR VECEU!!!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA!!!')
elif computador == 1: #PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 1:
        print('EMPATE!!!')
    elif jogador == 2:
        print('JOGADOR VECEU!!!')
    else:
        print('JOGADA INVALIDA!!!')
elif computador == 2: #TESOURA
    if jogador == 0:
        print('JOGADOR VECEU!!! ')
    elif jogador == 1:
        print('COMPUTADOR VECEU!!! ')
    elif jogador == 2:
        print('EMPATE!!!')
    else:
        print('JOGADA INVALIDA!!!')