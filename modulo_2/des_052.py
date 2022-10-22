n = int(input("Digite um número: "))
p = 0
for c in range(1, n+1):
    if n%c == 0:
        print("\033[33m {}\033[m".format(c), end="")
        p = p + 1
    else:
        print("\033[31m {}\033[m".format(c), end="")
print("\nO número {} foi dividido {} vezes.".format(n, p))
if p == 2:
    print("Portanto, ele É PRIMO!")
else:
    print("Portanto, ele NÃO É PRIMO!")

