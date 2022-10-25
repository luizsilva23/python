k = "S"
c = t = 0
while k == "S":
    c += 1
    n = int(input('Digite um número: '))
    t += n
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
           maior = n
        elif n < menor:
           menor = n
    k = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if k not in "SN":
        while k not in "SN":
            k = str(input('Opção inválida. Deseja continuar? [S/N]')).upper().strip()[0]
m = float(t/c)
print('Você digitou {} números e a média entre eles foi {:.1f}.'.format(c, m))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
