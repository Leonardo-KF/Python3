jogadores = []
jog = {}
g = []
while True:
    jog.clear()
    g.clear()
    jog['nome'] = str(input('Digite o nome do jogador: '))
    j = int(input('Digite o numero de jogos do jogador: '))
    for c in range(1, j+1):
        g.append(int(input(f'Numero de gols na partida {c}: ')))
    jog['gols'] = g[:]
    jog['total'] = sum(g)
    jogadores.append(jog.copy())
    while True:
        u = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        if u in 'SN':
            break
    if u == 'N':
        break
print('-='*20)
print('Cod ', end='')
for i in jog.keys():
    print(f'{i:<15}', end='')
print()
for i, v in enumerate(jogadores):
    print(f'{i:>2} ', end='')
    for c in v.values():
        print(f'{str(c):<16}', end='')
    print()
print('='*40)
while True:
    u = int(input('Digite o código do jogador que deseja mostrar os dados: '))
    if int(u) >= len(jogadores):
        print(f'Não existe nenhum jogador cadastrado com o código {u}! Tente novamente!')
    else:
        print(f'O jogador {jogadores[u]["nome"]} jogou {len(jogadores[u]["gols"])} partidas!')
        for c in range(0, len(jogadores[u]["gols"])):
            print(f' => Na partida {c+1} fez {jogadores[u]["gols"][c]} gols')
        while True:
            u1 = str(input('Deseja visualizar mais algum dado [S/N]? ')).strip().upper()[0]
            if u1 in 'SN':
                break
            print('Opção inválida! Digite novamente!')
        if u1 == 'N':
            break
print('Finalizando...')