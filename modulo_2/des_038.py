n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases de conversão: \n [ 1 ] Converter para BINÁRIO \n [ 2 ] Converter para OCTAL \n [ 3 ] Converter para HEXADECIMAL')
e = int(input('Sua opção: '))
if e == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(n, bin(n)[2:]))
elif e == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(n, oct(n)[2:]))
elif e == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('Opção Inválida. Tente novamente.')
