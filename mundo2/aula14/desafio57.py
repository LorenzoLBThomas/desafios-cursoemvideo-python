sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo [M/F]: ')).strip().upper()

print('Sexo {} registrado com sucesso.'.format(sexo.upper()))
