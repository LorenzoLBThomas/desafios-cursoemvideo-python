from datetime import date

ano_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade == 18:
    print('Você deve se alistar esse ano.')
elif idade < 18:
    print('Você deverá se alistar em {}.'.format(ano_nascimento + 18))
elif idade > 18:
    print('Você deveria ter se alistado em {}.'.format(ano_nascimento + 18))
