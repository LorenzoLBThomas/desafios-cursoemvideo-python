soma_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
mulheres_menos_de_20_anos = 0

for pessoas in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(pessoas))).strip()
    idade = int(input(('Digite a idade da pessoa: ')))
    sexo = str(input(('Digite o sexo da pessoa: '))).strip()
    print('')
    soma_idade += idade


    '''if pessoas == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_mais_velho = nome'''
    # Não entendi a necessidade desses códigos.

    if idade > maior_idade_homem and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_mais_velho = nome
    if idade < 20 and sexo in 'Ff':
        mulheres_menos_de_20_anos += 1
media_idade = soma_idade / 4

print('A média de idades das 4 pessoas foi de {:.0f} anos.'.format(media_idade))
print('O homem mais velho se chama {} e tem {} anos.'.format(nome_homem_mais_velho.title(), maior_idade_homem))
print('{} mulhers tem(têm) menos de 20 anos.'.format(mulheres_menos_de_20_anos))
