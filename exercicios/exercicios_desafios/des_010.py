r = float(input('Quanto dinheiro você tem? R$'))
vd = float(input('Quanto está valendo o dólar? '))
d = float(r/vd)
print('Com esse valor, você pode comprar US${:.2f}.'.format(d))
