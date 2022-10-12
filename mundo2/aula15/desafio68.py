from random import randint

print('-=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-=-' * 20)

cont = 0
while True:

    escolha_jogador = ' '
    while escolha_jogador not in 'PI':
        escolha_jogador = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()

    numero_jogador = int(input('Jogue um número: '))
    numero_computador = randint(0, 10)
    soma = numero_jogador + numero_computador
    print('DEU PAR!' if soma % 2 == 0 else 'DEU ÍMPAR!')
    if escolha_jogador == 'P':
        if soma % 2 == 0:
            print(f'Você ganhou, parabéns! Você jogou {numero_jogador}, e o computador jogou {numero_computador}. ')
            print('Vamos jogar novamente...')
            cont += 1
        if soma % 2 == 1:
            print(f'Você perdeu. Você jogou {numero_jogador}, e o computador jogou {numero_computador}.')
            break
    elif escolha_jogador == 'I':
        if soma % 2 == 1:
            print(f'Você ganhou, parabéns! Você jogou {numero_jogador}, e o computador jogou {numero_computador}.')
            print('Vamos jogar novamente...')
            cont += 1
        if soma % 2 == 0:
            print(f'Você perdeu. Você jogou {numero_jogador}, e o computador jogou {numero_computador}.')
            break

print(f'Você ganhou {cont} partida(s) consecutiva(s).')
