n = str(input('Digite um número: '))
n1 = n.rjust(4)

print('Unidade: ', n1[3:])
print('Dezena: ', n1[2:3])
print('Centena: ', n1[1:2])
print('Milhar: ', n1[:1])

# O professor fez:
# u = n // 1 % 10
# d = n // 10 % 10
# c = n // 100 % 10
# m = n // 1000 % 10
