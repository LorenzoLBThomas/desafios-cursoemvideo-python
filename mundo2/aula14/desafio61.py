print('-=-' * 20)
print(' GERADOR DE PROGRESSÃO ARITMÉTICA V2.0')
print('-=-'*20)

n1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = n1
cont = 1

while cont <= 10:
    print('{} - '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')


'''decimo_termo = n1 + (10 - 1) * razao

print(n1, end=' - ')
while n1 != decimo_termo:
    n1 += razao
    print(n1, end=' - ')
print('Fim')'''

# Foi a maneira que eu fiz. Está certo, mas tem uma sem usar a fórmula.
