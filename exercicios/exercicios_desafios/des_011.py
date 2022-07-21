b = float(input('Qual é o tamanho em metros da base da sua parede? '))
h = float(input('Qual é a altura em metros da sua parede? '))
a = b*h
tinta = a / 2

print('Para pintar sua parede de área {:.2f}m², serão necessários {:.2f} litros de tinta.'.format(a, tinta))
