valores = list()
maior = menor = cont = 0

for c in range(0, 5):
    valores.append(int(input('Digite um p: ')))

for num in valores:
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f'Você digitou os valores {valores}.')
print(f'O maior p digitado foi {maior}, e está na posição de número ', end='')
for n, v in enumerate(valores):
    if v == maior:
        print(n, end='...')
print(f'\nO menor p digitado foi {menor}, e está na posição de número ', end='')
for n, v in enumerate(valores):
    if v == menor:
        print(n, end='...')
