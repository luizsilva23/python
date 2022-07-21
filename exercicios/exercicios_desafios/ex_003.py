n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
mod = n1 % n2

print('A soma entre os valores vale {}, a diferença é de {}. \n O produto vale {}.'.format(s, sub, m), end=' ')
print('O resultado de divisão é {:.3f}, mas em uma divisão inteira seria {}, com o resto {}. O resultado da potenciação é {}'.format(d, di, mod, e))
