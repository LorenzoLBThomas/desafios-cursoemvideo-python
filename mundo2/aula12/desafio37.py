from time import sleep

n = int(input('Digite o número inteiro que deseja converter: '))
print('[ 1 ] para converter para binário.\n'
      '[ 2 ] para converter para octal.\n'
      '[ 3 ] para converter para hexadecimal.')
sleep(1)

escolha = int(input('Digite a opção desejada: '))

if escolha == 1:
    print(bin(n)[2:])
elif escolha == 2:
    print(oct(n)[2:])
elif escolha == 3:
    print(hex(n)[2:])
else:
    print('\033[31mNúmero inválido. Digite a opção desejada (entre 1 e 3).\n'
          'Código do erro: 1\033[m')
