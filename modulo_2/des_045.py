from random import choice
print('''SUAS OPÇÕES:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
j = int(input('Qual é a sua jogada? '))
c = choice([1, 2, 3])
print('JO')
print('KEN')
print('PO!')
print('{:-^20}'.format(' resultado '))
if j == 1:
    if c == 1:
        print('O computador também escolheu PEDRA')
        print('EMPATOU')
    elif c == 2:
        print('O computador escolheu PAPEL')
        print('Você PERDEU')
    elif c == 3:
        print('O computador escolheu TESOURA')
        print('Você VENCEU!')
if j == 2:
    if c == 1:
        print('O computador escolheu PEDRA')
        print('Você VENCEU')
    elif c == 2:
        print('O computador também escolheu PAPEL')
        print('EMPATOU')
    elif c == 3:
        print('O computador escolheu TESOURA')
        print('Você PERDEU!')
if j == 3:
    if c == 1:
        print('O computador escolheu PEDRA')
        print('Você PERDEU')
    elif c == 2:
        print('O computador escolheu PAPEL')
        print('Você VENCEU!')
    elif c == 3:
        print('O computador também escolheu TESOURA')
        print('EMPATOU')
print('{:-^20}'.format('fim'))
