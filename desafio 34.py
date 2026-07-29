nome = str(input('Digite o nome completo do seu funcionario: '))
salario = float(input('Digite o salario do funcionario {}: '.format(nome)))
if salario > 1250:
    print('Entao caro colaborador {}, seu salario é de {} você estara recebendo um aumento de 10% então seu salario ficou {}'.format(nome, salario, salario/10+salario))
if salario < 1250:
    print('Entao caro colaborador {}, seu salario é de {} você estara recebendo um aumento de 15% então seu salario ficou {}'.format(nome, salario, salario/15+salario))