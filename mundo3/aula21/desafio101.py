def voto(nasc=0):
    from datetime import date
    ''' Ao importar pra dentro da def, a importação só vale na função, economizando muita
        memória '''
    ano_atual = date.today().year
    idade = ano_atual - nasc
    if 18 <= idade < 65:
        return f'Com {idade} anos: Voto obrigatório'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto opcional'
    else:
        return f'Com {idade} anos: Voto negado'


ano_nasc = int(input('Digite seu ano de nascimento: '))
print(voto(ano_nasc))
