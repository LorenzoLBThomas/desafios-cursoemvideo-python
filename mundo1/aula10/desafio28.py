from random import randint
from time import sleep

n = randint(0,5)
print('-=-' * 20)
n1 = int(input('Adivinhe o número que o programa escolheu de 0 a 5: '))
print('-=-' * 20)
print('\033[35mPROCESSANDO...\033[m')
sleep(1)

if n1 == n:
    print('\033[32mVocê ganhou!\033[m O número que você escolheu foi "{}" e o número que o programa escolheu foi "{}"!'.format(n1, n))
else:
    print('\033[31mVocê perdeu.\033[m O número que você escolheu foi "{}", e o número que o programa escolheu foi "{}".'.format(n1, n))
