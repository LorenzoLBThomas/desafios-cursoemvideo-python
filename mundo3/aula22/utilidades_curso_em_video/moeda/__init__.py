def moeda(a, simb='R$'):
    a = f'{simb}{a:.2f}'
    return a


def aumentar(q, a, form=False):            # a irá ser a % a ser aumentada. Exemplo: se a for 10, aumentará 10% de q.
    n = q + (a / 100 * q)
    if form:
        return moeda(n)
    return n


def diminuir(q, s, form=False):           # s irá ser a % a ser subtraída. Exemplo:. se s for 10, diminuirá 10% de q.
    n = q - (s / 100 * q)
    if form:
        return moeda(n)
    return n


def dobro(q, form=False):
    n = q * 2
    if form:
        return moeda(n)
    return n


def metade(q, form=False):
    n = q / 2
    if form:
        return moeda(n)
    return n


def resumo(q, a, s):
    print(f'Preço analisado:      R$ {q}\n'
          f'Dobro do preço:       R$ {q * 2}\n'
          f'Metade do preço:      R$ {q / 2}\n'
          f'{a}% de aumento:      R$ {q + (a / 100 * q)}\n'
          f'{s}% de redução:      R$ {q - (s / 100 * q)}')
