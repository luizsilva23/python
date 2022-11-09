times = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense',
        'Corinthians', 'Athletico-PR', 'Atlético-MG', 'São Paulo',
        'Fortaleza', 'Botafogo', 'América-MG', 'Santos', 'Goiás',
        'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO',
        'Chapecoense', 'Juventude')
print('=-='*15)
print(f'Lista dos Times do Brasileirão: {times}')
print('=-='*15)
print(f'Os Cinco primeiros são: {times[0:5]}')
print('=-='*15)
print(f'Os quatro últimos são: {times[-4:]}')
print('=-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-='*15)
print(f'O time Chapecoense está na {times.index("Chapecoense")+1}ª posição')
