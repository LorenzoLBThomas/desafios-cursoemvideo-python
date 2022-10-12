from time import sleep
reta1 = float(input('Digite a medida de uma reta: '))
reta2 = float(input('Digite a medida de outra reta: '))
reta3 = float(input('Digite a medida da outra reta: '))
print('-=-' * 20)
print('Analisador de Triângulos v2.0')
print('-=-' * 20)
sleep(2)

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    if reta1 == reta2 and reta2 == reta3:
        print('Essas retas podem formar um triângulo, e ele será equilátero.')
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('Essas retas podem formar um triângulo, e ele será isósceles.')
    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
        print('Essas retas podem formar um triângulo, e ele será escaleno.')
else:
    print('Essas retas não podem formar um triângulo.')
