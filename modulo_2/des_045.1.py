from random import randint
from time import sleep
item = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}.'.format(item[computador]))
print('Jogador jogou {}.'.format(item[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATOU!')
    elif jogador == 1:
        print('Você VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR venceu!')
    else:
        print('Jogada Inválida!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR venceu!')
    elif jogador == 1:
        print('EMPATOU!')
    elif jogador == 2:
        print('Você VENCEU!')
    else:
        print('Jogada Inválida!')
elif computador == 2:
    if jogador == 0:
        print('Você VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR Venceu!')
    elif jogador == 2:
        print('EMPATOU!')
    else:
        print('Jogada Inválida!')