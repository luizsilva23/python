extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        else:
            print('Opção Inválida, tente novamente.')
    print(f'Você digitou o número {extenso[n]}.')
    r = str(input('Quer continuar? [S/N]').upper().strip()[0])
    if r == 'N':
        break
    while r not in'SN':
        print('Opção Inválida.')
        r = str(input('Quer continuar? [S/N]').upper().strip()[0])
