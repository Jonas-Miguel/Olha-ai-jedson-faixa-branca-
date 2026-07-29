f = str(input('Digite o nome do funcionario:'))
s = float(input('Digite o salario do colaborador:'))
a = float(input('Digite a porcentagem que ele recebera de almento:'))
r = (s * a)/100
sf = s + r
print('Então {} seu salario atualmente é de {}, certo, ai com o aumento de {} porcento ele vai ficar {} reais, ta bom,\npra você? '.format(f, s, a, sf))