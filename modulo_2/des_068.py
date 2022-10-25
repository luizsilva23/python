from random import randint
print('=-=' * 10)
print('  VAMOS JOGAR PAR OU IMPAR')
print('=-=' * 10)
c = 0
while True:
    comp = randint(0, 10)
    jog = int(input('Diga um valor: '))
    esc = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    n = comp + jog
    if n % 2 == 0 and esc == 'P':
        print('-' * 20)
        print(f'Você jogou {jog} e o computador escolheu {comp}. No total, {n}. DEU PAR')
        print('-' * 20)
        print('VOCÊ VENCEU!')
        c += 1
    elif n % 2 != 0 and esc == 'I':
        print('-' * 20)
        print(f'Você jogou {jog} e o computador escolheu {comp}. No total, {n}. DEU ÍMPAR')
        print('-' * 20)
        print('VOCÊ VENCEU!')
        c += 1
    elif n % 2 == 0 and esc == 'I':
        print('-' * 20)
        print(f'Você jogou {jog} e o computador escolheu {comp}. No total, {n}. DEU PAR')
        print('-' * 20)
        print('você PERDEU!')
        break
    elif n % 2 != 0 and esc == 'P':
        print('-' * 20)
        print(f'Você jogou {jog} e o computador escolheu {comp}. No total, {n}. DEU ÍMPAR')
        print('-' * 20)
        print('você PERDEU!')
        break
    else:
        print('invalido')
    print('Vamos jogar novamente...')
    print('=-=' * 10)
print(f'GAME OVER!! Você venceu {c} vezes.')
