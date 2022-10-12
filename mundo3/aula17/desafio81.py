valores = list()
cont = 0
while True:
    n = int(input('Digite um número: '))

    valores.append(n)
    cont += 1
    escolha_usuario = str(input('Quer continuar? [S/N]: ')).strip().upper()

    while escolha_usuario not in 'SN':
        escolha_usuario = str(input('Opção inválida. Quer continuar? [S/N]: ')).strip().upper()

    if escolha_usuario == 'N':
        break

print(f'Foram digitados {len(valores)} valores.')
valores.sort(reverse=True)
print(f'Em ordem decrescente, os valores digitados foram: {valores}')

if 5 in valores:
    print('O p "5" foi digitado.')
else:
    print('O p "5" não foi digitado.')
