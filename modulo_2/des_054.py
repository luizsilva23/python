from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    idade = int(input("Digite a idade da {}ª pessoa: ".format(c)))
    if ano-idade >= 21:
        maior += 1
    else:
        menor += 1
print("Ao todo tivemos {} pessoas MAIORES DE IDADE. \nE também tivemos {} pessoas MENORES DE IDADE.".format(maior, menor))
