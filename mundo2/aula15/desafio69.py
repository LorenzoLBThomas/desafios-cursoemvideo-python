cont_maiores = 0
cont_masculino = 0
cont_feminino_menos_20 = 0

while True:
    print('-=-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-=-' * 20)

    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()

    escolha_usuario = ' '

    while escolha_usuario not in 'SN':
        escolha_usuario = str(input('Deseja continuar? [S/N]: ')).strip().upper()

    if idade >= 18:
        cont_maiores += 1
    if sexo == 'M':
        cont_masculino += 1
    if sexo in 'F' and idade < 20:
        cont_feminino_menos_20 += 1
    if escolha_usuario == 'N':
        break

print(f'\n{cont_maiores} pessoas têm mais de 18 anos.')
print(f'{cont_masculino} pessoas do sexo masculino foram cadastradas.')
print(f'{cont_feminino_menos_20} pessoas do sexo feminino têm menos de 20 anos.')
