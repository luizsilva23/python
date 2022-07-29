print('Analisando Triângulos')
a = float(input('1º lado: '))
b = float(input('2º lado: '))
c = float(input('3º lado: '))
if a > b + c and b > a + c and c > a + b:
    print('As medidas forma um triângulo!')
else:
    print('As medidas são incapazes de formar um triângulo!')
