n = int(input('Digite um número para ver o seu fatorial: '))
fat = 1
print('Calculando {}! = '.format(n), end='')
for c in range(n, 0, -1):
    fat *= n
    print(n, end='')
    print(' x ' if c > 1 else ' = ', end='')
    n -= 1
print(fat)
