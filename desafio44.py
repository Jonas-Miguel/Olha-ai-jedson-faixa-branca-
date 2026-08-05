print('{:=^30}'.format('LOJAS JONAS EL MAIORAL'))
gasto = float(input('Qual o valor foi gasto na loja?($) '))
desconto = gasto - (gasto * 10 / 100)
desconto2 = gasto - (gasto * 5 / 100)
duas = gasto / 2
print('Qual sera a forma de pagamento? ')
escolha = int(input('''Qual das opções: 
[1] À vista dinheiro ou cheque
[2] À vista no cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão
Qual é a opção? '''))
if escolha == 1:
    print('Sua compra de {} reais tera um desconto de 10% e passara a custar {} reais!'.format(gasto, desconto))
elif escolha == 2:
    print('Sua compra de {} reais tera um desconto de 5% e passara a custar {} reais!'.format(gasto, desconto2))
elif escolha == 3:
    print('Sua compra de {} reais dividida em 2x ficara, 2x de {} reais'.format (gasto, duas))
elif escolha == 4:
    quantidade = int(input('Quantas parcelas? '))
    juros20 = (gasto / 10 * 2 + gasto)
    parcelas = juros20 / quantidade
    print('A sua compra parcelada em {} vezes, vai ficar {} reais por mes no total de {} reais'.format (quantidade,parcelas,juros20))
else:
    print('OPÇÃO INVALIDA PARA PAGAMENTO, TENTE NOVAMENTE COM OUTRA OPÇÃO')
    print('Sua compra ficou no total de R${:.2f} '.format(gasto))