def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número:
    :param num: Número cujo fatorial será calculado.
    :param show: (Opcional) Mostrar ou não mostrar a conta.
    :return: O p do fatorial de num.
    """

    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end ='')
            if c > 1:
                print(' x ', end='')
            else:
                print(f' = {f} ', end='')
    print()
    return f


n = int(input('Digite um número para calcular seu fatorial: '))
print(f'O fatorial de {n} é {fatorial(n, show=False)}.')
print()
help(fatorial)
