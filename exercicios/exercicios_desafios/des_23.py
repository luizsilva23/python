n = int(input('Digite um número entre 0 e 9999: '))
print('Analisando o número {}:'.format(n))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidades: ', u)
print('Dezenas: ', d)
print('Centenas: ', c)
print('Milhares: ', m)
