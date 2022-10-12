from time import sleep

c = ('\033[m',         # 0 = sem cor
     '\033[0;30;41m',   # 1 = vermelho
     '\033[0;30;42m',   # 2 verde
     '\033[0;30;45m')   # 3 roxo


def texto(msg, cor=0):
    print(c[cor], end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))
    print(c[0], end='')

escolha = ''
while True:
    texto('SISTEMA DE AJUDA', 2)
    escolha = str(input('Digite a função ou biblioteca com a(o) qual precisa de ajuda > ')).strip().lower()
    if escolha == 'fim':
        break
    sleep(0.5)
    texto(f'Acessando o manual do comando {escolha}', 3)
    sleep(1)
    help(escolha)

texto('Até logo', 1)
