ma = 0
n1 = int(input('Digite um valor: '))
if n1 > ma:
    ma = n1
me = n1
n2 = int(input('Digite outro: '))
if n2 > ma:
    ma = n2
if n2 < me:
    me = n2
n3 = int(input('Mais um: '))
if n3 > ma:
    ma = n3
if n3 < me:
    me = n3
print('O maior número foi: {}.'.format(ma))
print('O menor número foi: {}.'.format(me))
