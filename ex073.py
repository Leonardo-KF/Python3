tab = (
'Palmeiras', 'Atlético MG', 'Fortaleza', 'Bragantino', 'Flamengo', 'Atletico PR', 'Ceará', 'Santos', 'Atlético GO',
'Bahia', 'Corinthians', 'Fluminense', 'Juventude', 'Internacional', 'Sport Recife', 'Cuiaba', 'São Paulo', 'América MG',
'Grêmio', 'Chapecoense')
print('Os quatro primeiros colocados são')
for c in range(0, 4):
    print(tab[c])
print('\nOs quatro ultimos colocados são')
for c in range(16, 20):
    print(tab[c])
print('\nOs times em ordem alfabética são')
print(sorted(tab))
print(f'\nA chapecoense esta na {tab.index("Chapecoense") + 1}ª posição')
