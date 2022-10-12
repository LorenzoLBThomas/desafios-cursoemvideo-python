soma = cont = 0

while True:
    n = int(input('Digite um número inteiro (999 para parar): '))
    if n == 999:
        break
    else:
        cont += 1
        soma += n

print(f'Você digitou {cont} números (sem contar o 999), e a soma entre eles foi {soma} (desconsiderando o 999).')
# Eu acho mais fácil fazer esse programa de outro jeito, mas vou fazer assim para usar o break, que é o tema da aula.
