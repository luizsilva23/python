n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
m = (n1 + n2) / 2
if m < 7 and m > 5:
    print('O Aluno obteve média {:.1f} e está EM RECUPERAÇÃO.'.format(m))
elif m <=5:
    print('O aluno obteve média {:.1f} e está REPROVADO.'.format(m))
else:
    print('O Aluno obteve média {:.1f} e está APROVADO.'.format(m))
