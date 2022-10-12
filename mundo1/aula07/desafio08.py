m = float(input('Digite o p medido em metro(s): '))
print('A medida {} metro(s) é a mesma coisa que:'.format(m))
print('{} km\n{} hm\n{} dam\n{} dm\n{} cm\n{} mm'.format((m/1000), (m/100), (m/10), (m*10), (m*100), (m*1000)))
