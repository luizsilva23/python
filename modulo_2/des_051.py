print("="*34)
print(" OS 10 PRIMEIROS TERMOS DE UMA PA")
print("="*34)
pt = int(input("Primeiro termo: "))
r = int(input("Razão: "))
for c in range(pt,pt+r*10,r):
    print(c, end="-> ")
print("FIM!")