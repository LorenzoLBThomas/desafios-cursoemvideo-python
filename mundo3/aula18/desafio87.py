'''geral = list()
coluna0 = list()
coluna1 = list()
coluna2 = list()
cont1 = cont2 = cont3 = 0
fileira1 = list()

for c in range(0, 9):
    n = int(input(f'Digite um p para a posição [{cont1}] [{cont2}]: '))
    if cont2 == 0:
        coluna0.append(n)
    if cont2 == 1:
        coluna1.append(n)
    if cont2 == 2:
        coluna2.append(n)
    if cont1 == 1:
        fileira1.append(n)
    cont2 += 1
    if cont2 > 2:
        cont1 += 1
        cont2 = 0

geral.append(coluna0)
geral.append(coluna1)
geral.append(coluna2)

for num in geral:
    print(f'[  {num[0]}  ]', end='')
print()
for num in geral:
    print(f'[  {num[1]}  ]', end='')
print()
for num in geral:
    print(f'[  {num[2]}  ]', end='')

print('\n')

pares = list()
for num in geral:
    for par in num:
        if par % 2 == 0:
            pares.append(par)

print(f'A soma dos valores pares digitados é {sum(pares)}.')
print(f'A soma dos valores da terceira coluna é {sum(geral[2])}.')
print(f'O maior p da segunda linha é {max(fileira1)}.')'''


# Abaixo segue a maneira que eu fiz, baseado na maneira que o professor do Curso em Vídeo fez o desafio 86.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for fileira in range(0, 3):
    for coluna in range(0, 3):
        matriz[fileira][coluna] = int(input(f'Digite um p para [{fileira}, {coluna}]: '))

print('-=' * 30)

for fileira in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[fileira][coluna]:^5}]', end='')
    print()
pares = 0

for listas in matriz:
    for par in listas:
        if par % 2 == 0:
            pares += par

coluna3 = 0

for colunas in matriz:
    coluna3 += colunas[2]

maior_segunda_fil = matriz[1][0]

if matriz[1][1] > maior_segunda_fil:
    maior_segunda_fil = matriz[1][1]

elif matriz[1][2] > maior_segunda_fil:
    maior_segunda_fil = matriz[1][2]

print(f'A soma de todos os valores pares digitados é {pares}.')
print(f'A soma dos valores da terceira coluna é {coluna3}.')
print(f'O maior número na segunda linha é {maior_segunda_fil}.')
