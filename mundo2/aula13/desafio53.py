'''frase = str(input('Digite uma frase: ')).strip()
frase = frase.replace(' ', '')
frase_invertida = frase[::-1]

print('Frase invertida (sem espaços): {}'.format(frase_invertida))
if frase == frase_invertida:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')'''
# Esse foi o jeito que eu fiz, que é mais eficiente, mas vou colocar aqui usando o for.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(junto, inverso)

if junto == inverso:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')
