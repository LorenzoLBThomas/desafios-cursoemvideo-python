'''from math import factorial

n = int(input('Digite um número: '))

print('O fatorial do número {} é: {} '.format(n, factorial(n)))'''

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1 # Recebe um porque 1 é o fator nulo da multiplicação.

print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
