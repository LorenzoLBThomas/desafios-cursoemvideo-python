from time import sleep


def linha():
    print('-=' * 20)


def contador(inicio, fim, passo):
    cont = inicio
    if inicio < fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
        while cont <= fim:
            print(cont, end=' ')
            sleep(0.5)
            cont += passo
        print('FIM!')
    elif inicio > fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
        while cont >= fim:
            print(cont, end=' ')
            sleep(0.5)
            cont -= passo
        print('FIM!')


contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
n1 = int(input('Início: '))
n2 = int(input('Fim: '))
n3 = abs(int(input('Passo: ')))
if n3 == 0:
    n3 = 1
linha()
contador(n1, n2, n3)
