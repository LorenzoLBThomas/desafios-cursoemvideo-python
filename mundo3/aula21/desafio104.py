def leiaint(msg):
    num = str(input(msg))
    while not num.isnumeric():
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        num = str(input(msg))
    if num.isnumeric():
        num = int(num)
    return num


n = leiaint('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}.')
