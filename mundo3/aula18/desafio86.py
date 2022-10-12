'''geral = list()
coluna0 = list()
coluna1 = list()
coluna2 = list()
cont1 = cont2 = cont3 = 0

for c in range(0, 9):
    n = int(input(f'Digite um p para a posição [{cont1}] [{cont2}]: '))
    if cont2 == 0:
        coluna0.append(n)
    if cont2 == 1:
        coluna1.append(n)
    if cont2 == 2:
        coluna2.append(n)

    cont2 += 1
    if cont2 > 2:
        cont1 += 1
        cont2 = 0

geral.append(coluna0)
geral.append(coluna1)
geral.append(coluna2)

for num in geral:
    print(f'[{num[0]:^5}]', end='')
print()
for num in geral:
    print(f'[{num[1]:^5}]', end='')
print()
for num in geral:
    print(f'[{num[2]:^5}]', end='')'''
# A maneira acima foi como eu fiz. Funciona, mas a do professor tem bem menos linhas.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for fileira in range(0, 3):
    for coluna in range(0, 3):
        matriz[fileira][coluna] = int(input(f'Digite um p para [{fileira}, {coluna}]: '))

print('-=' * 30)

for fileira in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[fileira][coluna]:^5}]', end='')
    print()
