cont = 0

while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    print('-' * 30)
    for cont in range(0, 11):
        print(f'{n} x {cont} = {n * cont}')
    print('-' * 30)
print('\nFim do programa.')
