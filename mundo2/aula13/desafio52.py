n = int(input('Digite um número inteiro: '))
divisores = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m{}\033[m'.format(c), end=' ')
        divisores += 1
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')
if divisores == 2:
    print('\nO número {} foi divisível duas vezes, por isso é primo.'.format(n))
else:
    print('\nO número {} foi dividido {} vezes, por isso não é primo.'.format(n, divisores))
