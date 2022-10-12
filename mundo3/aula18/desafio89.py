boletim = list()
aluno = list()
cont = -1

while True:
    nome = str(input('Nome do aluno: ')).strip().upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    boletim.append([nome.title(), [nota1, nota2], media])
    cont += 1

    escolha_usuario = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while escolha_usuario not in 'SN':
        escolha_usuario = str(input('Opção inválida. Deseja continuar? [S/N]: ')).strip().upper()
    if escolha_usuario == 'N':
        break
print(cont)
print('-=-' * 4)
print('Boletim:')
print('-=-' * 4)

print(f'{"Num.":<7}{"Nome":<10}{"Média":>8}')
print('-' * 25)

for i, a in enumerate(boletim):
    print(f'{i:<7}{a[0]:<10}{a[2]:>8.1f}')

while True:
    escolha_usuario2 = str(input('\nDeseja mostrar as notas que compõe a média de algum aluno? [S/N]: ')).strip().upper()
    while escolha_usuario2 not in 'SN':
        escolha_usuario2 = str(input('Opção inválida. Deseja mostrar as notas que compõe a média de algum aluno? [S/N]:'
                                     ' ')).strip().upper()
    if escolha_usuario2 == 'N':
        break

    escolha_usuario3 = int(input('\nMostrar notas de qual aluno? (Utilize o número do aluno conforme o boletim acima): '))
    while escolha_usuario3 > cont:
        print('\nNão existe um aluno que corresponde a esse número. Tente novamente.')
        escolha_usuario3 = int(input('\nMostrar notas de qual aluno? (Utilize o número do aluno conforme o '
                                     'boletim acima): '))
    print(f'\nNotas de {boletim[escolha_usuario3][0]}: {boletim[escolha_usuario3][1]}')
