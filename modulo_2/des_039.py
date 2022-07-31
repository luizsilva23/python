from datetime import date
n = int(input('Ano de Nascimento: '))
i = date.today().year - n
print('Quem nasceu em {} tem {} anos.'.format(n, i))
if i < 18:
    print('Ainda faltam {} anos para o seu alistamento.'.format(18 - i))
    print('Seu alistamento será em {}.'.format(n + 18))
elif i == 18:
    print('Você deve se alistar ainda este ano.')
else:
    print('Você já deveria ter se alistado há {} anos.'.format(i - 18))
    print('Seu alistamento foi em {}.'.format(n + 18))
