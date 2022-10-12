from math import trunc

n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(n, trunc(n)))


# Abaixo está como eu fiz da primeira vez, mas como acho que o professor quer que o desafio seja feito utilizando o módulo Math, vou refazer do jeito que acho que ele quer.

# n = float(input('Digite um número:'))
# print('O número {} tem a parte inteira {:.0f}.'.format(n, n))
