total_idade = float(0)
idade_hvelho = 0
nome_hvelho = ""
m20 = 0
for c in range(1,5):
    print("-"*5, end=' ')
    print("{}ª PESSOA".format(c), end=" ")
    print("-"*5)
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    total_idade = total_idade + idade
    genero = str(input("Gênero [M/F]: "))
    if c == 1 and genero == "M":
        idade_hvelho = idade
        nome_hvelho = nome
    elif genero == "M" and idade > idade_hvelho:
        idade_hvelho = idade
        nome_hvelho = nome
    elif genero == "F" and idade < 20:
        m20 = m20 + 1
print("A média de idade do grupo é de {:.1f} anos.".format(total_idade/5))
print("{} é o homem mais velho.".format(nome_hvelho))
print("{} mulheres têm menos de 20 anos.".format(m20))

