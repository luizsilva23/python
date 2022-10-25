k = ''
m20 = hom = p18 = 0

while True:
    while k != 'N':
        print('-=-'*10)
        print('    CADASTRE UMA PESSOA')
        print('-=-'*10)

        idade = int(input('Idade: '))

        # Input Sexo
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
        while sexo not in 'MF':
            print('Opção Inválida. Tente novamente.')
            sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

        print('-' * 30)

        # CONTAGEM DE PESSOAS
        if idade >= 18:
           p18 += 1
        if sexo == 'M':
           hom += 1
        if idade < 20 and sexo == 'F':
            m20 += 1

        # Adicionar pessoas
        k = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        while k not in 'NS':
            print('Opção inválida, tente novamente.')
            k = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    break

# Output
print(f'Total de {p18} com 18 anos ou mais.')
print(f'Ao todo temos {hom} homens cadastrados.')
print(f'E temos {m20} mulheres com menos de 20 anos.')
