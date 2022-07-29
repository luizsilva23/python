d = float(input('Qual é a distância da viagem? '))
if d < 200:
    print('Você está prestes a começar uma viagem de {}Km. \nO valor da passagem será de R${:.2f}.'.format(d, d*0.5))
else:
    print('Você está prestes a começar uma viagem de {}Km. \nO valor da passagem será de R${:.2f}.'.format(d, d * 0.45))

