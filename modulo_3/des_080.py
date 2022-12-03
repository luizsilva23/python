n = []
for c in range(0, 5):
    x = int(input('Digite um valor: '))
    if c == 0:
        n.append(x)
        print('Adicionado no final da lista...')
    else:
        if x > n[c-1]:
            n.append(x)
            print('Adicionado no final da lista...')
        if x < n[0]:
            n.insert(0, x)
            print('Adicionado na posição 0 da lista.')
        if n[0] < x < n[c]:
            n.insert(n[], x)
print(n)