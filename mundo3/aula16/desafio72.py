num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
               'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número inteiro de 0 a 20: '))

    while n < 0 or n > 20:
        n = int(input('Tente novamente. Digite um número inteiro de 0 a 20: '))

    print(f'Você digitou o número {num_extenso[n]}.')

    escolha_usuario = str(input('Quer continuar? [S/N]: ')).strip().upper()

    while escolha_usuario not in 'SN':
        escolha_usuario = str(input('Opção inválida. Quer continuar? [S/N]: ')).strip().upper()
    if escolha_usuario == 'N':
        break
