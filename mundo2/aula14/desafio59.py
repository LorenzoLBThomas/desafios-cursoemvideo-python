n1 = float(input('Digite um p: '))
n2 = float(input('Digite um p: '))

escolha_usuario = 0

while escolha_usuario != 5:

      print('[ 1 ] para somar'
            '\n[ 2 ] para multiplicar'
            '\n[ 3 ] para descobrir qual é o maior'
            '\n[ 4 ] para escolher novos valores'
            '\n[ 5 ] para sair do programa')

      escolha_usuario = int(input('Digite a opção desejada: \n'))

      maior_numero = n1
      if n2 > n1:
            maior_numero = n2

      if escolha_usuario == 1:
            print('A soma dos valores digitados é {}.\n'.format(n1 + n2))
      if escolha_usuario == 2:
            print('A multiplicação dos valores digitados é {}.\n'.format(n1 * n2))
      if escolha_usuario == 3:
            print('O maior número digitado é o número {}.\n'.format(maior_numero))
      if escolha_usuario == 4:
            n1 = float(input('Digite um p: '))
            n2 = float(input('Digite um p: '))
      if escolha_usuario > 5 or escolha_usuario < 1:
            print('Opção inválida. Tente novamente.\n')

print('Fim do programa.')
