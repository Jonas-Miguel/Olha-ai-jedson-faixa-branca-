p = str(input('Qual produto você quer converter? '))
v  = float(input('Digite o valor do produto: '))
d1 = float(input('Qual a porcentagen do desconto? '))
d = (v * d1) / 100
r = v - d
print (' O {} com {} porcento de desconto fica {} reais'.format(p, d1, r))