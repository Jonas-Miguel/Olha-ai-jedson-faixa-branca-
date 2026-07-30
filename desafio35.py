r1 = float(input('Digite cumprimento da primeira reta: '))
r2 = float(input('Digite o cumprimento da segunda reta: '))
r3 = float(input('Digite o cumprimento da terceira reta: '))
if (r1 == r2) and (r1 == r3)  and (r2 == r3):
    print('As retas informadas formam um triangulo, EQUILATERO')
elif (r1 == r2 != r3) and (r1 == r3 != r2)  and (r2 == r3 != r1 ):
    print('As retas indicadas formam um triangulo ISÓCELES')
elif (r1 + r2 ) > r3 or (r1 + r3 ) > r2 or (r2 + r3 ) > r1 :
    print('As retas indicadas NÃO PODEM forman um triangulo ')
elif r1 != r2 != r3 != r1:
    print('As retas informadas forman um triangulo ESCALENO')