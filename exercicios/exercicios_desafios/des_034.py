s = float(input('Qual é o salário do funcionário? R$'))
if s > 1250:
    ns = s + (s/100*10)
if s <= 1250:
    ns = s + (s/100*15)
print('O novo salário é de R${:.2f}.'.format(ns))
