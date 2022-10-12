from datetime import date

# Considerar que para se aposentar, são necessários 35 anos de contribuição.

trabalhador = dict()

trabalhador['Nome'] = str(input('Digite o nome do trabalhador: ')).strip().title()
ano_nasc = int(input('Digite o ano de nasicmento: '))
trabalhador['Idade'] = date.today().year - ano_nasc
trabalhador['ctps'] = int(input('Digite o número da carteira de trabalho (0 caso não tenha): '))

if trabalhador['ctps'] != 0:
    trabalhador['Contratação'] = int(input('Digite o ano de contratação: '))
    trabalhador['Salário'] = float(input('Digite o salário: R$ '))
    trabalhador['Idade_Aposentadoria'] = (trabalhador['Contratação'] + 35) - ano_nasc

print('-=' * 30)

for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}.')
