from time import sleep
laco_programa = True
while laco_programa == True:
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    laco_menu = True
    while laco_menu == True:
        sleep(1)
        print('=-=' * 10)
        print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos valores\n[5] sair')
        menu = int(input('>>>>> Qual a sua opção? '))
        print('=-=' * 10)
        if menu == 1:
            print('A soma entre {} e {} é: {}'.format(n1, n2, n1 + n2))
        elif menu == 2:
            print('O produto de {} e {} é: {}'.format(n1, n2, n1 * n2))
        elif menu == 3:
            if n1 < n2:
                print('Entre os valores {} e {}, o maior é: {}'.format(n1, n2, n2))
            elif n1 > n2:
                print('Entre os valores {} e {}, o maior é: {}'.format(n1, n2, n1))
            else:
                print('Os valores são iguais.')
        elif menu == 4:
            print('Insira os novos valores:')
            laco_menu = False
        elif menu == 5:
            print('Finalizando...')
            sleep(1.5)
            laco_programa = False
            laco_menu = False
        else:
            print('Opção Inválida, tente novamente')
print('Fim do Programa')
