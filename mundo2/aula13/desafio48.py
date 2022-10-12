soma = 0
cont = 0

for c in range(3, 501, 3):
    if c % 2 == 1:
        soma = soma + c
        cont = cont + 1
print('A soma dos {} valores solicitados é: {}'.format(cont, soma))
