x = float(input('Primeiro Segmento: '))
y = float(input('Segundo Segmento: '))
z = float(input('Terceiro Segmento: '))
if x + y > z and x + z > y and z + y > x:
    if x == y == z:
        print('As medidas PODEM FORMAR um triângulo EQUILÁTERO.')
    elif x != y != z != x:
        print('As medidas PODEM FORMAR um triângulo ESCALENO.')
    else:
        print('As medidas PODEM FORMAR um triângulo ISÓSCELES.')
else:
    print('Essas medidas não formam um triângulo.')
