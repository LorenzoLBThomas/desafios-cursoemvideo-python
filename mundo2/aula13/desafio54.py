from datetime import date
ano_atual = date.today().year
menores = 0
maiores = 0

for c in range (0, 7):
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    if ano_atual - ano_nascimento < 18:
        menores += 1
    else:
        maiores += 1
print('Das pessoas nascidas nos anos digitados a cima, {} são menores de idade, e {} são maiores de idade.'.format(menores, maiores))
