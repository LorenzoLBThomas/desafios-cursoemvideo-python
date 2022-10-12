import sys
from random import randint
from time import sleep

jogador = str(input('Escolha: Pedra, Papel ou Tesoura? ')).strip()
computador = randint(1, 3)
escolha_computador = ''

if computador == 1:
    escolha_computador = 'PEDRA'
if computador == 2:
    escolha_computador = 'PAPEL'
if computador == 3:
    escolha_computador = 'TESOURA'

if jogador.upper() == 'PEDRA' or jogador.upper() == 'PAPEL' or jogador.upper() == 'TESOURA':
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!')
else:
    sys.exit('Opção inválida!\nVocê deve escolher Pedra, Papel ou Tesoura. Tente novamente.\nCódigo do erro: 1')

print('-=' * 11)
print('Computador jogou {}'.format(escolha_computador.title()))
print('Você jogou {}'.format(jogador.title()))
print('-=' * 11)

if escolha_computador == jogador.upper():
    print('Empate! Tanto você, quanto o computador escolheram {}!'.format(jogador.lower()))
if escolha_computador == 'PEDRA' and jogador.upper() == 'TESOURA':
    print('Você perdeu! Pedra ganha de tesoura!')
elif escolha_computador == 'PAPEL' and jogador.upper() == 'PEDRA':\
    print('Você perdeu! Papel ganha de pedra!')
elif escolha_computador == 'TESOURA' and jogador.upper() == 'PAPEL':\
    print('Você perdeu! Tesoura ganha de papel!')
elif escolha_computador != jogador.upper():
    print('Você ganhou! {} ganha de {}.'.format(jogador.title(), escolha_computador.title()))
