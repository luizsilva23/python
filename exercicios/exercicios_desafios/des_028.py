from random import randint
from time import sleep
print('Vou pensar em um número de 0 a 5. Você consegue adivinhar?')
nj = int(input('Em qual número pensei? '))
nc = randint(0, 5)
print('Processando...')
sleep(2)
if nj == nc:
    print('ACERTOU! Você venceu')
else:
    print('Você errou... \nO número que eu pensei foi {}.'.format(nc))
