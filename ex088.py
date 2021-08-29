from random import randint
from time import sleep
jogo = []
tj = []
print('='*34)
nj = int(input('Quantos jogos você deseja sortear? '))
print('='*34)
print(f'SORTEANDO {nj} JOGOS')
while True:
    sleep(0.7)
    jogo.clear()
    for c in range(0, 6):
        n = randint(1, 60)
        if n in jogo:
            n = randint(1, 60)
        jogo.append(n)
        jogo.sort()
    tj.append(jogo)
    print(f'Jogo {len(tj)}: {tj[len(tj) - 1]}')
    if nj == len(tj):
        break
print('='*10, 'Boa sorte!', '='*10)