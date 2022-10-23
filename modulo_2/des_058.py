from random import randint
computador = int(randint(0, 10))
print("Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?")
acertou = False
tentativas = 0
while acertou == False:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... Tente outra vez.')
        else:
            print('Mais... Tente outra vez.')
print('Você acertou em {} tentativas. Parabéns!'.format(tentativas))
