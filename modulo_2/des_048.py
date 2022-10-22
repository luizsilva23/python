s = 0
t = 0
for c in range(0, 501, 3):
    if c%2 !=0:
        s += c
        t += 1
print("O somatório dos {} números é: {}.".format(t, s))
