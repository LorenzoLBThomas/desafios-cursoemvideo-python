from desafios.mundo3.aula23.desafio115.lib.interface import *
from desafios.mundo3.aula23.desafio115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquvioexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        print(leraquivo(arq))
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(2)
