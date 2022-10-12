from time import sleep


def maior(* valores):
    cont = mai = 0
    for n in valores:
        if cont == 0:
            mai = n
        elif n > mai:
            mai = n
        cont += 1
    print('-=' * 30)
    print('Analisando os valores passados...')
    for v in valores:
        print(v, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor digitado foi {mai}.')
    sleep(1)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
