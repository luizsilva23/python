palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
            'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
            'PRATICAR', 'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')
for n in palavras:
    print(f'\nNa palavra {n} temos ', end='')
    for letra in n:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')

