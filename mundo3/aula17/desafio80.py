valores = list()

for c in range(0, 5):
    n = int(input('Digite um número: '))

    if c == 0 or n > max(valores):
        valores.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos}.')
                break
            pos += 1

print(f'\nOs valores digitados, em ordem, foram: {valores}.')
