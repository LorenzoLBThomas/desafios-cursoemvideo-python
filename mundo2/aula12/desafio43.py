peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é {:.1f} e você está abaixo do peso ideal.'.format(imc))
elif imc >= 18.5 and imc <= 24.9:
    print('Seu IMC é {:.1f} e você está no peso ideal'.format(imc))
elif imc >= 25 and imc <= 29.9:
    print('Seu IMC é {:.1f} e você está em sobrepeso'.format(imc))
elif imc >= 30 and imc <= 39.9:
    print('Seu IMC é {:.1f} e você está com obesidade'.format(imc))
elif imc >= 40:
    print('Seu IMC é {:.1f} e você está com obesidade mórbida.'.format(imc))
