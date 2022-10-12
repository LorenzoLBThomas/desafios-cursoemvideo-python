def escreva(txt):
    tam = len(txt) + 4 # Para deixar uma borda (dois a mais para cada lado)
    print('~' * tam)
    print(f'  {txt}')  # Para centralizar.
    print('~' * tam)


escreva('Olá, Mundo!')
escreva('Curso de Python')
