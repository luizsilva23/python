n = []
n.append(int(input('Digite um Valor: ')))
while True:
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp in 'SN':
        if resp == 'S':
            novo = int((input('Digite outro valor: ')))
            if novo in n:
                print('Valor repetido, não vou adicionar.')
            else:
                n.append(novo)
                print('Valor adicionado com sucesso.')
        else:
            break
    else:
        print('Resposta Inválida. Tente Novamente.')
print('=-='*25)
n.sort()
print(f'Você digitou os valores: {n}')
