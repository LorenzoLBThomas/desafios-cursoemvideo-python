num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))

print(f'\nO número 9 apareceu {num.count(9)} vez(es).')
if 3 in num:
    print(f'O primeiro número 3 foi digitado na posição de número {num.index(3) + 1}.')
else:
    print('O número 3 não foi digitado.')

print('Os números pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

# NÃO CONSEGUI FAZER SOZINHO.
