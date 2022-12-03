n = []
for c in range(0, 5):
    n.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=-=' * 15)

print(f'Os valores digitados foram {n}.')
print(f'O maior número digitado foi: {max(n)}, na posição ', end='')
for i, v in enumerate(n):
    if v == max(n):
        print(f'{i}... ', end='')
print(f'\nO menor número digitado foi: {min(n)}, na posição ', end='')
for i, v in enumerate(n):
    if v == min(n):
        print(f'{i}...', end='')
