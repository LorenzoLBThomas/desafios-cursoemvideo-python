n = 0
contador = 0
soma = 0

while n != 999:
    n = int(input('Digite um número inteiro [999 para parar]: '))
    if n != 999:
        soma += n
        contador += 1

print('Você digitou {} números (antes do 999) e a soma entre eles foi {} (desconsiderando o 999).'.format(contador, soma))
