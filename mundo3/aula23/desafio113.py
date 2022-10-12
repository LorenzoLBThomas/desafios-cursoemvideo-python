def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


num_int = leiaint('Digite um valor inteiro: ')
num_real = leiafloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {num_int} e o número real foi {num_real}.')
