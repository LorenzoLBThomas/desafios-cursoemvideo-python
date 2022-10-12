largura = float(input('Qual é a largura da parede (em metros)? '))
altura = float(input('Qual é a altura da parede (em metros)? '))
area = largura*altura
print('Uma parede com {} metros de largura, e {} metros de altura, tem {} metros quadrados.'.format(largura, altura, area))
print('Para pintar essa parede serão necessários {} litros de tinta.'.format(area/2))
# O professor pediu para considerar que cada litro de tinta pinta uma área de 2 metros quadrados.
