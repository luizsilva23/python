print('-'*23)
print('Sequência de Fibonacci')
print('-'*23)
t = int(input('Quantos termos você quer mostrar? '))
a = 0
b = 1
cont = 3
print('~' * 30)
print('{} -> {} -> '.format(a, b), end='')
while cont < t:
    c = a + b
    print(c, end=' -> ')
    a = b
    b = c
    cont += 1
print('FIM')
print('~' * 30)
