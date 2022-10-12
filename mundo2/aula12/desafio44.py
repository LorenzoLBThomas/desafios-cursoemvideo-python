from time import sleep

preco_normal = float(input('Digite o preço do produto: R$ '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista no dinheiro ou no cheque (10% de desconto)\n'
      '[ 2 ] à vista no cartão (5% de desconto)\n'
      '[ 3 ] em 2x no cartão (Preço normal)\n'
      '[ 4 ] em 3x ou mais no cartão. (20% de juros)')
sleep(2)

forma_de_pagamento = int(input('Digite a opção desejada: '))

if forma_de_pagamento == 1:
    preco_final = preco_normal * 90/100
    print('O preço final do produto é R${}.'.format(preco_final))
elif forma_de_pagamento == 2:
    preco_final = preco_normal * 95/100
    print('O preço final do produto é R${}.'.format(preco_final))
elif forma_de_pagamento == 3:
    preco_final = preco_normal
    print('O preço final do produto é R${}, que será divido em duas vezes de R$ {} sem juros.'.format(preco_final, preco_final / 2))
elif forma_de_pagamento == 4:
    parcelas = int(input('Digite a quantidade de parcelas: '))
    preco_final = preco_normal * 120/100
    print('O preço final do produto é R${}, que será divido em {} vezes de R$ {} com juros.'.format(preco_final, parcelas, preco_final / parcelas))
else:
    print('Digite uma opção válida (entre 1 e 4).')
