s = c = 0
while True:
    n = int(input('Digite um número. [999 para finalizar]: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} valores foi de {s}.')
