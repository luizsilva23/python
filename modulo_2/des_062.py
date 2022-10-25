print('Gerador de PA')
print('=-='*10)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = 0
c = 10
c2 = 10
while c2 != 0:
    while c != 0:
        print('{} -> '.format(n), end='')
        n += r
        c -= 1
        t += 1
    print('PAUSA')
    c2 = int(input('Quantos termos você quer mostrar a mais? '))
    c = c2
print('Progressão finalizada com {} termos mostrados.'.format(t))
