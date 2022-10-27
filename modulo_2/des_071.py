n50 = n20 = n10 = n1 = 0
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
n = int(input('Que valor você quer sacar? R$'))
while True:
    if n - 50 >= 0:
        n = n - 50
        n50 += 1
    elif n - 20 >= 0:
        n -= 20
        n20 += 1
    elif n - 10 >= 0:
        n -= 10
        n10 += 1
    elif n - 1 >= 0:
        n -= 1
        n1 += 1
    elif n == 0:
        break
print('-'*32)

if n50 > 0:
    print(f'Total de {n50} cédulas de R$50.')
if n20 > 0:
    print(f'Total de {n20} cédulas de R$20')
if n10 > 0:
    print(f'Total de {n10} cédulas de R$10')
if n1 > 0:
    print(f'Total de {n1} cédulas de R$1')