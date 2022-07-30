casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = float(input('Quantos anos de financiamento? '))
parcela = float(casa / (tempo * 12))
maximo = salario / 100 * 30
print('Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}.'.format(casa, tempo, parcela))

if parcela <= maximo:
    print('EMPRESTIMO APROVADO')
else:
    print('EMPRESTIMO NEGADO')
