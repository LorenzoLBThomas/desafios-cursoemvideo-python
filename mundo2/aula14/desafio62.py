print('-=-' * 20)
print('GERADOR DE PROGRESSÃO ARITMÉTICA V3.0')
print('-=-' * 20)

n1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = n1
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa...')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

# Não consegui fazer esse desafio sozinho.
# Apenas conseugi fazer o código abaixo, que só perguntava uma vez a quantidade de termos a mais que o usuário queria mostrar.



'''decimo_termo = n1 + (10 - 1) * razao

print(n1, end=' - ')
while n1 != decimo_termo:
    n1 += razao
    print(n1, end=' - ')
print('Pausa...')

escolha_usuario = int(input(('Quer mostrar mais quantos termos?: ')))

while n1 != decimo_termo + escolha_usuario * razao:
    n1 += razao
    print(n1, end=' - ')
print('Fim.')'''

# Maneira que eu fiz, mas não deu certo. O programa só perguntava uma vez se queria ver mais termos.
