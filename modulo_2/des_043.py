p = float(input('Peso: (KG)'))
a = float(input('Altura: (M)'))
i = p / a**2
print('Seu IMC é de {:.1f}.'.format(i))
if i > 40:
    print('OBESIDADE MÓRBIDA')
elif 40 >= i > 30:
    print('Obesidade')
elif 30 >= i > 25:
    print('SOBREPESO')
elif 25 >= i >= 18.5:
    print('PESO IDEAL')
elif i < 18.5:
    print('ABAIXO DO PESO')
