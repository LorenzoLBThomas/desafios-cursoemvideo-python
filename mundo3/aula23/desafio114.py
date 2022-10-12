import requests

try:
    requests.get('http://www.pudim.com.br')
except requests.exceptions.ConnectionError:
    print('\033[30mO site pudim.com.br não está acessível no momento.\033[m')
else:
    print('\033[32mO site pudim.com.br está acessível no momento.\033[m')
