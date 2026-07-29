n1 = int(input('Digite um numero inteiro qualquer: '))
n2 = int(input('Digite outro numero inteiro qualquer: '))
if n1 > n2:
    print('O numero {} é maior que o {}:'.format(n1,n2))
elif n1 < n2:
    print('O numero {} é maior que o numero {}:'.format(n2,n1))
elif n1 == n2:
    print('Os dois numeros são iguais, nen um é maior ou menor que o outro!')