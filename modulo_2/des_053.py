frase = str(input("Digite uma frase: "))
frase = frase.upper().strip().split()
frase = "".join(frase)
inverso = ""
for letra in range(len(frase) -1, -1, -1):
    inverso += (frase[letra])
print("A frase que você digitou foi {}. Ao contrário ela fica {}.".format(frase, inverso))
if frase == inverso:
    print("Sendo assim, a frase É UM PALÍNDROMO.")
else:
    print("Sendo assim, a frase NÃO É UM PALÍNDROMO.")
