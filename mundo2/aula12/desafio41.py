from datetime import date
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano_nascimento

if idade <= 9:
    print('A categoria desse atleta é: Mirim')
elif idade > 9 and idade <= 14:
    print('A categoria desse atleta é: Infantil')
elif idade > 14 and idade <= 19:
    print('A categoria desse atleta é: Junior')
elif idade > 19 and idade <= 20:
    print('A categoria desse atleta é: Sênior')
elif idade > 20:
    print('A categoria desse atleta é: Master')
