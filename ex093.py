jog = {}
g = []
jog['nome'] = str(input('Digite o nome do jogador: '))
j = int(input('Digite o numero de jogos do jogador: '))
for c in range(1, j+1):
    g.append(int(input(f'Numero de gols na partida {c}: ')))
jog['gols'] = g[:]
jog['total'] = sum(g)
print(jog)
print('-='*20)
for k, v in jog.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {jog["nome"]} jogou {len(jog["gols"])} partidas')
for c in range(1, j+1):
    print(f'  => Na partida {c}, fez {jog["gols"][c-1]} gols!')
print(f'Foi um total de {jog["total"]} gols.')
# for i, c in enumerate(jogador["gols"]):
    # print(f'  => Na partida {i}, fez {v} gols')