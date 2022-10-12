jogador = dict()
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
gol = list()

for c in range(1, jogador['partidas'] + 1):
    gol.append(int(input(f'Quantos gols na partida {c}?: ')))

jogador['gols'] = gol[:]
jogador['num_gols'] = sum(gol)

print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for c, g in enumerate(jogador['gols']):
    print(f'      => Na partida {c+ 1}, fez {g} gol(s).')
print(f'Fez um total de {jogador["num_gols"]} gols.')
