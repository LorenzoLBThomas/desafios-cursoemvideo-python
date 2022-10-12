from math import radians, sin, cos, tan

angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O seno, o cosseno e a tangente de {:.2f} é:'.format(angulo))
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(seno, cosseno, tangente))
