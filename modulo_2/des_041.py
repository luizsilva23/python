from datetime import date
n = int(input('Ano de nascimento: '))
i = date.today().year - n
print('O atleta tem {} ano(s).'.format(i))
if i <= 9:
    print('Classificação: MIRIM')
elif 9 < i <= 14:
    print('Classificação: INFANTIL')
elif 14 < i <= 19:
    print('Classifação: JUNIOR')
elif 19 < i <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')
