import math
co = int(input('Qual o comprimento do cateto oposto? '))
ca = int(input(' Qual o comprimento do cateto adjacente? '))
h = math.hypot(co, ca)
seno = math.acos(co/h)
coseno = math.cos(ca / h)
tangente = math.tan(co / ca)
print('Levando en consideração essas medidas a hipotenusa é {}'.format(h))
print ('O valor de seno {}\nCoseno {}\nTangente {}'.format(seno, coseno, tangente))
