t = n = x = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        t += n
        x += 1
print('Você digitou {} números e a soma foi igual a: {}.'.format(x, t))
