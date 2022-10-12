n = int(input('Digite um número: '))

print('A tabuada do {} é: '.format(n))
print('-' * 12)

for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
