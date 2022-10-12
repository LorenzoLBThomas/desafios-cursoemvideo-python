n1 = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
decimo_termo = n1 + (10 - 1) * razao

for c in range(n1, decimo_termo + 1, razao):
    print(c)
