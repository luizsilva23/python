maior = 0
menor = 0
peso = 0
for c in range(1, 6):
    peso = float(input("Digite o peso da {}ª pessoa: ".format(c)))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        else:
            maior = peso
print("O maior peso lido foi de {}kg\nO menor peso lido foi de {}kg.".format(maior, menor))
