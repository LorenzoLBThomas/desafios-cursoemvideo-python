from random import randint

num_computador = randint(1, 10)
num_jogador = 0
tentativas = 0

print('-=-' * 20)
print('JOGO DA ADIVINHAÇÃO!')
print('-=-' * 20)

num_jogador = int(input('Tente acertar o número inteiro que o computador escolheu (entre 1 e 10): '))
tentativas += 1

while num_jogador > num_computador:
    num_jogador = int(input('Menos... Tente acertar o número inteiro que o computador escolheu (entre 1 e 10): '))
    tentativas += 1

while num_jogador < num_computador:
    num_jogador = int(input('Mais... Tente acertar o número inteiro que o computador escolheu (entre 1 e 10): '))
    tentativas += 1
print('\nVocê acertou! O número que o computador escolheu foi {}.'.format(num_computador))
print('Você precisou de {} tentativa(s) para acertar.'.format(tentativas))
