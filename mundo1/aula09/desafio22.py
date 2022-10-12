nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em letras maiúsculas é:', nome.upper())
print('Seu nome em letras minúsculas é:', nome.lower())

nomesemespacos = nome.replace(' ', '')
print('Seu nome tem, ao todo, {} letras.'.format(len(nomesemespacos))) # O professor fez essa etapa com .format(len(nome) - nome.count(' ')

nomedividido = nome.split()

print('Seu primeiro nome é {} e tem {} letras.'.format(nome.split()[0], len(nomedividido[0])))
