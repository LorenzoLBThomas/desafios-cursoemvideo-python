reta1 = float(input('Digite a medida de uma reta: '))
reta2 = float(input('Digite a medida de outra reta: '))
reta3 = float(input('Digite a medida da outra reta: '))
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Essas três retas \033[32mpodem formar um triângulo\033[m!')
else:
    print('Essas três retas \033[31mnão podem formar um triângulo\033[m.')
