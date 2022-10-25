print('Construtor de PA')
print('=-='*12)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
while c != 10:
    print('{} -> '.format(n), end='')
    n = n + r
    c += 1
print('FIM')
