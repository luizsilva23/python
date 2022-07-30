print('\033[31mOlá, Mundo!\033[m')
print('\033[41mTestando Cores\033[m')
print('\033[7mEfeito negativo\033[m')
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'fundobranco': '\033[7;40m'}

print('Teste de {}cores{} usando {}dicionários{}.'.format(cores['azul'], cores['limpa'], cores['fundobranco'], cores['limpa']))
