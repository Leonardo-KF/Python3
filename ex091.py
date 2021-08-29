from random import randint
from time import sleep
from operator import itemgetter
jog = {}
for c in range(1, 5):
    jog[f"jogador {c}"] = randint(1, 6)
rank = []
rank = sorted(jog.items(), key=itemgetter(1), reverse=True)
print('Valores Sorteados')
for k, v in jog.items():
    print(f'{k} tirou {v} no dado!')
    sleep(0.7)
print('='*30)
print('O Ranking é:')
for i, v in enumerate(rank):
        print(f'{i + 1}° Lugar: {v[0]} com {v[1]}')
        sleep(0.7)
