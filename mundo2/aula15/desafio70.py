total = 0
produtos_mais_de_mil = 0
produto_mais_barato = ''
preco_mais_barato = 0
cont = 0

while True:
    nome_produto = str(input('Digite o nome do produto: ')).strip().title()
    preco = float(input('Digite o preço do produto: R$ '))
    escolha_usuario = ' '

    while escolha_usuario not in 'SN':
        escolha_usuario = str(input('Quer continuar? [S/N]: ')).strip().upper()

    cont += 1
    total += preco

    if cont == 1 or preco < preco_mais_barato: # Juntei dois if em um só. Vi essa dica na resolução do exercício no Curso Em Vídeo.
        preco_mais_barato = preco
        produto_mais_barato = nome_produto

    if preco > 1000:
        produtos_mais_de_mil += 1

    if escolha_usuario == 'N':
        break

print(f'\nO total da compra foi de R$ {total:.2f}.')
print(f'{produtos_mais_de_mil} produto(s) custou(aram) mais de mil reais!')
print(f'O produto mais barato foi {produto_mais_barato}, que custa R$ {preco_mais_barato:.2f}.')
