from math import cos, sin, tan, radians
ang = float(input('Qual é o ângulo? '))
print('O Seno de {:.1f} é igual a {:.2f}.'.format(ang, sin(radians(ang))))
print('O Cosseno de {:.1f} é igual a {:.2f}.'.format(ang, cos(radians(ang))))
print('A Tangente de {:.1f} é igual a {:.2f}.'.format(ang, tan(radians(ang))))
