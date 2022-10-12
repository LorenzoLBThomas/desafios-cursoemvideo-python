def notas(lst):
    """
    -> A função analisa notas de vários alunos recebidas de uma lista do programa principal.
    :param lst: Lista recebida do programa principal.
    :return: Retorna um dicionário contendo informações sobre a quantidade de notas,
    a maior e a menor nota, a média e a situação da turma.
    Criada por Lorenzo Lái Barboza Thomas.
    """
    media = sum(lst) / len(lst)
    retorno = {'total': len(lst), 'maior': max(lst), 'menor': min(lst), 'media': f'{media:.2f}'}
    escolha_sit = str(input('Deseja mostrar a situação da turma? [S/N]: ')).strip().upper()
    while escolha_sit not in 'SN':
        escolha_sit = str(input('Opção inválida. Deseja mostrar a situação da turma? [S/N]: ')).strip().upper()
    if escolha_sit == 'S':
        if media >= 7:
            retorno['situacao'] = 'Boa'
        elif media >= 6:
            retorno['situacao'] = 'Mediana'
        else:
            retorno['situacao'] = 'Ruim'
    return retorno


turma = list()
num = 1
while True:
    turma.append(float(input(f'Digite a nota do aluno {num}: ')))
    num += 1

    escolha_usuario = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while escolha_usuario not in 'SN':
        escolha_usuario = str(input('Opção inválida. Deseja continuar? [S/N]: ')).strip().upper()
    if escolha_usuario == 'N':
        break

print()
print(notas(turma))
print()
help(notas)
# Fiz de um jeito bem mais complicado do que ele pediu (fiz com input, ele fez sem).
