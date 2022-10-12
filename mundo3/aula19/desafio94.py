pessoa = dict()
pessoas = list()
#feminino = list()
idade_acima_media = list()

while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()

    #if pessoa['sexo'] == 'F':
        #feminino.append(pessoa['nome'])

    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Opção inválida. Digite o sexo [M/F]: ')).strip().upper()

    pessoas.append(pessoa.copy())
    pessoa.clear()

    escolha_usuario = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while escolha_usuario not in 'SN':
        escolha_usuario = str(input('Opção inválida. Deseja continuar? [S/N]: ')).strip().upper()
    if escolha_usuario == 'N':
        break

print(f'- Foram cadastradas {len(pessoas)} pessoas.')

soma_idades = 0
for i in pessoas:
    soma_idades += i['idade']
media = soma_idades / len(pessoas)

print(f'- A média de idade do grupo é de {media} anos.')

#print(f'As pessoas do sexo feminino são: {feminino}') Eu acho mais elegante e fácil mostrar assim, mas vou fazer como o professor do Curso em Vídeo mostrou.

print('- As pessoas do sexo femino são:', end=' ')


for f in pessoas:
    if f['sexo'] == 'F':
        print(f['nome'], end=' ')
print()

print('- Lista das pessoas que estão acima da média de idade:')

for i in pessoas:
    if i['idade'] > media:
        print()
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')

print()

#print(f'A(s) pessoa(s) com idade acima da média é(são): {idade_acima_media}') De novo, eu preferia fazer assim, mas vou fazer como o professor mostrou.
