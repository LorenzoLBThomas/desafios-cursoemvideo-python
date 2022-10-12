# Não consegui fazer sozinho.

print('-=-' * 20)
print('SEQUÊNCIA DE FIBONACCI')
print('-=-' * 20)

n = int(input('Quantos termos da Sequência de Fibonacci você quer mostrar? '))

t1 = 0
t2 = 1
cont = 3

print('{} - {} - '.format(t1, t2), end='')

while cont <= n:
    t3 = t1 + t2
    cont += 1
    t1 = t2
    t2 = t3
    print('{} - '.format(t3), end='')

print('Fim')
