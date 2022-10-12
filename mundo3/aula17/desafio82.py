valores = list()
pares = list()
impares = list()

while True:
    n = int(input('Digite um p: '))
    valores.append(n)

    escolha_usuario = str(input('Deseja continuar? [S/N]: ')).strip().upper()

    while escolha_usuario not in 'SN':
        escolha_usuario = str(input('Opção inválida. Deseja continuar? [S/N]: ')).strip().upper()

    if escolha_usuario == 'N':
        break

for v in valores:
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'Os valores digitados foram: {valores}.')
print(f'Os valores pares digitados foram: {pares}.')
print(f'Os valores ímpares digitados foram: {impares}.')

# Fiz primeiro com tudo no loop while, já alimentando as três listas, mas refiz depois alimentando apenas a primeira lista no loop while
# e analisando depois a lista, separando os pares dos ímpares.
