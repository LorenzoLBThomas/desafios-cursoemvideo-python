from desafios.mundo3.aula23.desafio115.lib.interface import cabecalho


def arquvioexiste(nome):
    try:
        a = open(nome, 'rt')  # r = read, t = text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')  # w = write, t = text, + cria o arquivo caso não exista
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')


def leraquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao lero arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado!')
