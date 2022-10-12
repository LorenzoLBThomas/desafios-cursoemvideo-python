# RESOLUÇÃO QUE EU FIZ

valor = int(input('Digite o p a ser sacado: '))
quant_50 = valor // 50
valor -= 50 * quant_50
quant_20 = valor // 20
valor -= 20 * quant_20
quant_10 = valor // 10
valor -= 10 * quant_10
quant_01 = valor // 1
valor -= 1 * quant_01

print('Você receberá:')
if quant_50 > 0:
    print(f'{quant_50} cédulas de R$ 50,00.')
if quant_20 > 0:
    print(f'{quant_20} cédulas de R$ 20,00.')
if quant_10 > 0:
    print(f'{quant_10} cédulas de R$ 10,00.')
if quant_01 > 0:
    print(f'{quant_01} cédulas de R$ 1,00.')



# RESOLUÇÃO DO CURSO EM VÍDEO ESTÁ AQUI EM BAIXO. EU ACHEI MUITO MAIS FÁCIL FAZER DO JEITO QUE EU FIZ, MAS NA RESOLUÇÃO ELE UTILIZA WHILE E BREAK.

valor = int(input('Qual p você quer sacar? R$ '))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
