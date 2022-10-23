n = int(input('Digite um número para calcular seu fatorial: '))
print('Calculando {}! = '.format(n), end='')
fat = 1
while n != 0:
    a = n
    n = n-1
    fat = fat * a
    if n != 0:
        print(a, "x ", end='')
    else:
        print(a, end='')
print(' = ', fat)

