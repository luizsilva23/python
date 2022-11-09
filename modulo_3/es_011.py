valores = []
for cont in range(0,5):
    valores.append(input('Digite um número: '))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')