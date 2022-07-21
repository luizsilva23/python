n = float(input('Digite um valor em metros: '))
c = n * 100
de = n * 10
m = n * 1000
d = n / 10
h = n / 100
k = n / 1000

print("O valor {} em metros vale {} centímetros, {} milímetros e decimetros vale {}.".format(n, c, m, de))
print('O valor {} em metros representa {} decâmetros, {} hectômetros e {} kilometros.'.format(n, d, h, k))