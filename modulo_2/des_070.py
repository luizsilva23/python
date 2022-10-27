r = ' '
t = c = i = b = 0

print('-' * 35)
print('        LOJA SUPER BARATÃO')
print('-' * 35)

while True:

# CADASTRO DE PRODUTOS
    nome = str(input('Nome do Produto: ')).strip()
    i += 1
    valor = float(input('Preço: R$'))

# CONTAGEM
    t += valor

    if valor > 1000:
        c += 1

    if i == 1:
        b = valor
        nb = nome
    else:
        if b > valor:
            b = valor
            nb = nome

# RESPOSTA
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r not in 'SN':
        while True:
            print('Opção inválida.')
            r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
            if r in 'SN':
                break
    if r == 'N':
        break

# OUTPUT
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${t:.2f}')
print(f'Temos {c} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nb} que custou R${b:.2f}.')
