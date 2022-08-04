print('{:-^30}'.format('Loja'))
valor = float(input('Valor das compras: R$'))
print('FORMAS DE PAGAMENTO')
print("""[ 1 ] à vista dinheiro/cheque 
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais cartão""")
o = int(input('Qual é a opção? '))
if o == 1:
    total = valor - (valor / 100 * 10)
elif o == 2:
    total = valor - (valor / 100 * 5)
elif o == 3:
    total = valor
    parcela = valor / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(parcela))
elif o == 4:
    parcela = int(input('Quantas parcelas? '))
    juros = float(valor * 0.2)
    total = valor + juros
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(parcela, total/parcela))
else:
    print('Opção Inválida')
    total = valor
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, total))
