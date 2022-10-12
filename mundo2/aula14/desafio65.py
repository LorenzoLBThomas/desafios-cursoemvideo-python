n = 0
escolha_usuario = 'S'
soma = 0
maior = 0
menor = 0
quantidade = 0

while escolha_usuario == 'S':
    n = int(input('Digite um número inteiro: '))
    soma += n
    quantidade += 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    escolha_usuario = str(input('Quer continuar? [S/N]: ')).upper().title().strip()

media = soma / quantidade

print('\nVocê digitou {} números.'.format(quantidade))
print('A média entre os números digitados foi {:.2f}.'.format(media))
print('O maior número entre os números digitados foi {}, e o menor foi {}.'.format(maior, menor))
