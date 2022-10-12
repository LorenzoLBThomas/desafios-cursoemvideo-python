salario = float(input('Qual é o salário do funcionário? R$ '))

if salario > 1250:
    print('Esse funcionário receberá um aumento de 10%, e seu novo salário será 2033[32mR${:.2f}\033[m.'.format(salario * 110/100))
else:
    print('Esse funcionário receberá um aumento de 15%, e seu novo salário será \033[32mR${:.2f}\033[m.'.format(salario * 115/100))
