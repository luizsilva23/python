from math import hypot
c1 = float(input("Digite o cateto adjacente: "))
c2 = float(input('Digte o cateto oposto: '))
print("A hipotenusa vai medir {:.2f}.".format(hypot(c1, c2)))
