v = float(input('Qual é a velocidade atual do carro? '))
if v > 80:
    m = (v - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h.')
    print('Você deverá pagar uma multa de R${:.2f}.'.format(float(m)))
else:
    print('Tenha um bom dia! Dirija com segurança.')
