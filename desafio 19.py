import random
print (' Galera vamos estar sorteando quem vai apagar o quadro hoje!')
a1 = str(input('Diga o primeiro aluno? '))
a2 = str(input('Diga o segundo aluno? '))
a3 = str(input('Diga o terceiro aluno? '))
a4 = str(input('Por fim diga o quarto e ultimo aluno? '))
nomes = [a1, a2, a3, a4]
s = random.choice(nomes)
print (' O aluno sorteado hoje Foi {}'.format(s))