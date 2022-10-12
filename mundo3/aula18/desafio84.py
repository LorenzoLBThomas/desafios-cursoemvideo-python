pessoas = list()
dados = list()

while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso [em KG]: ')))
    pessoas.append(dados[:])
    dados.clear()

    escolha_usuario = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while escolha_usuario not in 'SN':
        escolha_usuario = str(input('Opção inválida. Deseja continuar? [S/N]: ')).strip().upper()
    if escolha_usuario == 'N':
        break

print(f'{len(pessoas)} pessoas foram cadastradas.')

cont = 0
nome_maior = list()
nome_menor = list()
peso_maior = peso_menor = 0
for p in pessoas:
    cont += 1
    if cont == 1:
        nome_maior.append(p[0])
        nome_menor.append(p[0])
        peso_maior = p[1]
        peso_menor = p[1]
    else:
        if p[1] > peso_maior:
            nome_maior.clear()
            nome_maior.append(p[0])
            peso_maior = p[1]
        elif p[1] < peso_menor:
            nome_menor.clear()
            nome_menor.append(p[0])
            peso_menor = p[1]
        elif p[1] == peso_maior:
            nome_maior.append(p[0])
        elif p[1] == peso_menor:
            nome_menor.append(p[0])

print(f'O maior peso foi {peso_maior} KG. Peso de {nome_maior}.')
print(f'O menor peso foi {peso_menor} KG. Peso de {nome_menor}.')

# O professor fez de maneira diferente. A maneira dele tem menos linhas. Verificar no vídeo.
