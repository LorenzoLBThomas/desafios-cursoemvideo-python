geral = list()    # Seria possível também fazer: geral = [[], []]
pares = list()
impares = list()


for c in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

pares.sort()
impares.sort()

geral.append(pares)
geral.append(impares)

print(f'Os números pares digitados foram: {geral[0]}.')
print(f'Os número ímpares digitados foram: {geral[1]}.')
