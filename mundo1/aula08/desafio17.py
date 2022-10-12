from math import hypot

cateto1 = float(input('Digite a medida de um cateto: '))
cateto2 = float(input('Digite a medida do outro cateto: '))

print('A medida da hipotenusa desse triângulo é {:.2f}.'.format(hypot(cateto1, cateto2)))
