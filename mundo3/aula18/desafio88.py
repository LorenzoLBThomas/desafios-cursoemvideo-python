from random import randint
from time import sleep

geral = list()
num = list()
jogos = int(input('Quantos jogos você quer sortear?: '))
cont = 0

for j in range(0, jogos):
    for c in range(0, 6):
        n = randint(1, 60)
        while n in num:
            n = randint(1, 60)
        if n not in num:
            num.append(n)
    num.sort()
    geral.append(num[:])
    num.clear()
    sleep(1)

    print(f'Jogo {cont + 1}: {geral[cont]}')
    cont += 1
