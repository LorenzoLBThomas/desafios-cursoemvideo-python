times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará SC',
         'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')

print(f'Os cinco primeiros colocados do Brasileirão de 2021 são: {times[0:5]}.')
print(f'\nOs último quatro colocados do Brasileirão de 2021 são: {times[-4:]}.')
print(f'\nOs times do Brasileirão 2021 em ordem alfabética são: {sorted(times)}.')

#for pos, time in enumerate(times):     Foi o jeito que eu fiz, mas tem um jeito mais fácil.
    #if time == 'Chapecoense':
        #print(f'\nA Chapecoense ficou na posição de número {pos + 1}.')

print(f'\nA chapecoense está na posição de número {times.index("Chapecoense") + 1}.')
