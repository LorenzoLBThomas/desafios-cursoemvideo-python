soma_pares = 0
cont = 0
for c in range (0, 6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma_pares = soma_pares + n
        cont = cont + 1
print('Você digitou {} números pares, e a soma entre eles é {}. Os números ímpares foram desconsiderados.'.format(cont, soma_pares))
