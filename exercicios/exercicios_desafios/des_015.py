d = int(input('Quantos dias o carro foi alugado?' ))
km = float(input('Quantos Km foram percorridos? '))
t = (d * 60) + (km * 0.15)
print('O total a ser pago é de: R${:.2f}.'.format(t))
