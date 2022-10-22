s = 0
t = 0
for c in range(1, 7):
    n = int(input("Digite um número: "))
    if n%2 == 0:
        t = t + 1
        s = s + n
print("A soma dos {} números pares digitados é igual a {}.".format(t, s))
