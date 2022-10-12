velocidade = float(input('Informe a velocidade do carro em km/h: '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('Você foi \033[31mmultado\033[m! O carro estava a {:.1f} km/h, enquanto a velocidade máxima era 80 km/h'.format(velocidade))
    print('Você deverá pagar R${:.2f} de multa.'.format(multa))
