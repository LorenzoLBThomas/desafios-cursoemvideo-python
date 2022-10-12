from random import randint
from time import sleep
numeros = list()


def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(0, 10))
    print('Os números sorteados foram: ', end='')
    for n in numeros:
        print(n, end=' ')
        sleep(0.5)
    print()


sorteia(numeros)


def somapar(lista):
    soma = 0
    for p in lista:
        if p % 2 == 0:
            soma += p
    print(f'A soma dos números pares sorteados é {soma}.')


somapar(numeros)
