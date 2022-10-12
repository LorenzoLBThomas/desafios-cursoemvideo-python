aluno = dict()
aluno['Nome'] = str(input('Digite o nome do aluno: ')).strip().title()
aluno['Média'] = float(input('Digite a média do aluno: '))
if 6 <= aluno['Média'] < 7:
    aluno['Situação'] = 'recuperação'
elif aluno['Média'] < 6:
    aluno['Situação'] = 'reprovado'
else:
    aluno['Situação'] = 'aprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
