from random import shuffle

aluno1 = str(input('Digite o nome do aluno: '))
aluno2 = str(input('Digite o nome do aluno: '))
aluno3 = str(input('Digite o nome do aluno: '))
aluno4 = str(input('Digite o nome do aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print('A ordem de apresentação dos alunos será:\n{}'.format(lista))
