n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))

maior = n1
menor = n1

print('Analisando os números digitados, conclui-se que:')
# Eu poderia ter usado "and" também.
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('O maior número é {}'.format(maior))

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print('O menor número é {}'.format(menor))
