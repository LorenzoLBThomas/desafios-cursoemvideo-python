palavras = ('quero', 'ser', 'um', 'programador')

for c in palavras:
    print(f'\nNa palavra {c.upper()} temos as vogais: ', end='')
    for letras in c:
        if letras.lower() in 'aeiou':       # Não aceita acentos, pois não coloquei todas as vogais com todos os acentos nessa linha.
            print(f'{letras}', end=' ')

# Não consegui fazer sozinho.
