nome = str(input('\033[0;33mQual o nome do aluno?\033[m ')).title()
n1 = float(input('\033[0;33mQual foi a primeira nota do {} ?\033[m '. format(nome)))
n2 = float(input('\033[0;33mE a segunda nota?\033[m '))
media = (n1+n2)/2
if media >= 7:
    print('Parabens {}, sua média foi {} e Você foi aprovado com sucesso!'.format(nome,media))
elif 7 > media >= 5 :
    print('Então {}, sua média foi {}, e voce tera que ficar de recuperação!'.format(nome,media))
elif media < 5:
    print('caro aluno {}, a sua media foi {}, e infelizmente você foi reprovado!'.format(nome,media))