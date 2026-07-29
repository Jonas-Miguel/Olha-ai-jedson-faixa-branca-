import random
print (' Iremos fazer um sorteio para ver qual será a sequencia dos alunos que vao estar apresentando o trabalho')
a1 = str(input('Digite o nome do primeiro aluno?'))
a2= str(input('Segundo nome?'))
a3 = str(input('Terceiro nome?'))
a4 = str(input('Quarto nome?'))
nomes = [a1, a2, a3, a4]
s = random.shuffle(nomes) # embaralhar a lista direto
print('\nOrdem de apresentação')
print(f'1°: {nomes[0]}')
print(f'2°: {nomes[1]}')
print(f'3°: {nomes[2]}')
print(f'4°: {nomes[3]}')