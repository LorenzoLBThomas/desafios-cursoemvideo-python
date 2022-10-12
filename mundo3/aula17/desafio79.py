valores = list()

while True:
    n = int(input('Digite um número: '))
    while n in valores:
        print('Esse p já está na lista. Tente outro.')
        n = int(input('Digite um número: '))

    valores.append(n)

    escolha_usuario = str(input('Deseja continuar? [S/N]: ')).strip().upper()

    while escolha_usuario not in 'SN':
        escolha_usuario = str(input('Opção inválida. Deseja continuar? [S/N]: ')).strip().upper()

    if escolha_usuario == 'N':
        break
valores.sort()
print(f'Os valores digitados, em ordem crescente, foram: {valores}.')
