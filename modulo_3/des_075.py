num = (int(input('Digite um número: ')), int(input('Digite outro: ')), int(input('Digite mais um: ')), int(input('Digite o último: ')))
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na posição {num.index(3) + 1}.')
else:
    print('O valor três não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
