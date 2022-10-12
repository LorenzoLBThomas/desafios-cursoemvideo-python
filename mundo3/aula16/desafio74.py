from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os números sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')

#cont = menor = maior = 0             NÃO PRECISO FAZER ASSIM. POSSO USAR O MAX E O MIN
#for c in num:
    #cont += 1
    #if cont == 1:
        #maior = c
        #menor = c

    #if c > maior:
        #maior = c
    #if c < menor:
        #menor = c

print(f'\n\nO maior número sorteado foi {max(num)}.')
print(f'O menor número sorteado foi {min(num)}.')
