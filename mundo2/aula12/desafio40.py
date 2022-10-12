n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('Esse aluno(a) obteve média {:.1f} e está reprovado(a).'.format(media))
elif media >= 5 and media < 7:
    print('Esse aluno(a) obteve média {:.1f} e está de recuperação.'.format(media))
elif media >= 7:
    print('Esse aluno(a) obteve média {:.1f} e está aprovado(a).'.format(media))
