produtos_e_precos = ('Caderno', 25, 'Estojo', 65, 'Pasta', 50, 'Agenda', 39.90)

print('-' * 40)
print('LISTAGEM DE PREÇOS')
print('-' * 40)

for pos in range(0, len(produtos_e_precos)):
    if pos % 2 == 0:
        print(f'{produtos_e_precos[pos]:.<30}', end='')
    else:
        print(f'R${produtos_e_precos[pos]:.2f}')






'''print(produtos_e_precos[0], '................. R$', produtos_e_precos[1])
print(produtos_e_precos[2], '................. R$', produtos_e_precos[3])
print(produtos_e_precos[4], '................. R$', produtos_e_precos[5])
print(produtos_e_precos[6], '................. R$', produtos_e_precos[7])

print('-' * 40)'''
# Maneira que eu fiz, mas não é a mais eficiente.
