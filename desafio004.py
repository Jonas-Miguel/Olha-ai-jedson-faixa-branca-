n1 = int (input('\033[0;31mDigite um valor:\033[m '))
n2 = int (input('\033[0;32mDigite outro valor:\033[m '))
s = n1 + n2
print('A soma entre \33[0;30m{}\033[m e \033[0;32m{}\033[m vale \033[4;33;40m{}\033[m'.format(n1, n2, s))