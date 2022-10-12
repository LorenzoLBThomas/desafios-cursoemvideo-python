n = int(input('Digite um número para calcular seu fatorial: '))
f = 1

print('Calculando {}! = {} x'.format(n, n), end=' ')

for c in range(n-1, 0, -1):
    f *= c
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end='')
print(f * n)
