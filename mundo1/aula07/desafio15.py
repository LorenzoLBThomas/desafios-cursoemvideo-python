dias = int(input('O carro foi alugado por quantos dias? '))
kmrodados = float(input('Quantos km foram rodados com o carro durante o aluguel?'))
preco = (dias * 60) + (kmrodados * 0.15)

print('O p total a pagar é: R${:.2f}.'.format(preco))
