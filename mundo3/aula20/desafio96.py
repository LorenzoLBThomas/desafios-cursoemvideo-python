def area(larg, compr):
    a = larg * compr
    print(f'A área de um terreno {larg} x {compr} é de {a} metros quadrados.')


print('Controle de terrenos')
print('-' * len('Controle de terrenos'))
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
print()

area(largura, comprimento)
