frase = 'Curso em Vídeo Python'
print(frase[6])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:14:2])
print(frase[::3])

print("""Nessa aula,vamos aprender operações com String no Python.
As principais operações que vamos aprender são o
Fatiamento de String, Análise com Nessa aula,vamos aprender operações com String no Python.
As principais operações que vamos aprender são o
Fatiamento de String, Análise com Nessa aula,vamos aprender operações com String no Python.
As principais operações que vamos aprender são o
Fatiamento de String, Análise com""")

print(len(frase))
print(frase.count('r'))
print(frase.upper().count('O'))

print(frase.replace('Python', 'Android'))
print(frase)
frase = frase.replace('Curso', 'Cursando')
print(frase)

print('python' in frase)
print(frase.lower().find('python'))
print(frase.find('Python'))

dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2][3])
print('.'.join(dividido))



