s = float(input('Diga o seu salario: R$ '))
c = float(input('Digite o vador da casa que deseja comprar: R$ '))
a = int(input('Em quantos anos desesa pagar essa casa? '))
m = a * 12
p = c / m
salario = (s / 10) * 3
if p > salario:
    print('Infelizmente nao iremos conseguir liberar essa carta de credito para o senhor, a parcela da casa ficara em {}'
          '\ne 30 % do seu salario ficara em {} '.format(p, salario))
else:
    print('Olha so a parcela da casa ficara em {}, e 30% do seu salario ficara em {}, ficamos muito felize em aprovar'
          'essa carta de credito.'.format(p, salario))