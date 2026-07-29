cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
nome = input ('{}Digite o nome do aluno:{} '.format(cores['amarelo'],(cores['limpa'])))
nota1 = float(input('Digite a nota da primeira prova de{}:'.format(nome)))
nota2 = float(input('Digite a nota da segunda prova de {}:'.format(nome)))
print ('A media do aluno {} é {}'.format(nome, (nota1+nota2)/2))