# Não consegui fazer sozinho

expressao = str(input('Digite a expressão: '))

count_abrindo = count_fechando = 0

pilha = list()

#for simb in expressao:
    #if simb == '(':
        #count_abrindo += 1

    #elif simb == ')':
        #count_fechando += 1

for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida em termos de parênteses.')
else:
    print('Sua expressão não está válida em termos de parênteses.')

#if count_abrindo == count_fechando:
    #print('Sua expressão está válida em termos de parênteses.')
#else:
    #print('Sua expressão não está válida em termos de parênteses.')

# O que está como comentário foi a maneira que eu fiz. Acho até que não fiz sozinho, mas foi como eu fiz.
# Porém essa maneira não identifica como erro parênteses abertos e fechados em ordem errada. Exemplo: )1+1(
