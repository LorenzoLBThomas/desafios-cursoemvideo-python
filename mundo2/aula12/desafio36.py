valor = float(input('Qual é o p do imóvel: R$ '))
renda = float(input('Qual é sua renda mensal: R$ '))
anos = float(input('Em quantos anos você quer pagar esse imóvel? '))
prestacao = valor / (anos * 12)

if prestacao <= renda * 30 / 100:
    print('Seu empréstimo foi aprovado! Parabéns!')
else:
    print('Infelizmente seu empréstimo foi negado, pois o p da prestação excede 30% da sua renda.')
