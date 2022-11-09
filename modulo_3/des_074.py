from random import randint

sort = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram: ', end='')
for n in sort:
    print(f'{n} ', end='')
print(f'\nO maior valor foi: {max(sort)}.')
print(f'O menor valor foi: {min(sort)}.')
