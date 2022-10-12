def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Digite o nome do jogador: ')).strip().title()
g = str(input('Digite quantos gols o jogador fez no campeonato (numeral): '))
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
