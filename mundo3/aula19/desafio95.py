# Não consegui terminar sozinho.

jogador = dict()
jogadores = list()
gol = list()
cont = -1

while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    for c in range(1, jogador['partidas'] + 1):
        gol.append(int(input(f'Quantos gols na partida {c}?: ')))
        jogador['gols'] = gol[:]
        jogador['total'] = sum(gol)

    jogadores.append(jogador.copy())
    gol.clear()
    cont += 1

    escolha_usuario = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while escolha_usuario not in 'SN':
        escolha_usuario = str(input('Opção inválida. Deseja continuar? [S/N]: ')).strip().upper()
    if escolha_usuario == 'N':
        break

print('-=' * 30)
print('Núm. ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
#print(f'{"Núm.":<7}{"Nome":<10}{"Gols":>8}{"Total":>10}')
print('-' * 60)

for k, n in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in n.values():
        print(f'{str(d):<15}', end='')
    print()


#for i, n in enumerate(jogadores):
    #print(f'{i:<7}{n["nome"]:<10}{n["total"]:>10}')
    #{n["gols"]:>8} Não tá funcionando.

escolha_usuario2 = str(input('\nDeseja mostrar os dados de algum jogador? [S/N]: ')).strip().upper()
while True:
    while escolha_usuario2 not in 'SN':
        escolha_usuario2 = str(input('Opção inválida. Deseja mostrar os dados de algum jogador? [S/N]:'))\
            .strip().upper()

    if escolha_usuario2 == 'N':
        break

    escolha_usuario3 = int(input('Deseja ver os dados de qual jogador? (Utilize o número do jogador conforme a tabela'
                                 ' acima): '))
    while escolha_usuario3 > cont or escolha_usuario3 < 0:
        print('\nNão existe um jogador que corresponde a esse número. Tente novamente.')
        escolha_usuario3 = int(input('\nMostrar notas de qual jogador? (Utilize o número do aluno conforme a '
                                     'tabela acima): '))
    print()
    print(f'-- DADOS DO JOGADOR {jogadores[escolha_usuario3]["nome"].upper()}:')

    for c, g in enumerate(jogadores[escolha_usuario3]['gols']):
        print(f'Na partida {c+1} fez {g} gols.')

    escolha_usuario2 = str(input('\nDeseja mostrar os dados de algum jogador? [S/N]: ')).strip().upper()
