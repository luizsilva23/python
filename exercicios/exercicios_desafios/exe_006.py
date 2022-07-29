n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
m = (n1 + n2) / 2
print('Sua média é igual a: {:.1f}'.format(m))
if m >= 6.0:
    print('Aluno APROVADO')
else:
    print('Aluno REPROVADO')