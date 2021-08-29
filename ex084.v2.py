pessoas = list()
dados = list()
mp = ml = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso em kg: ')))
    if len(dados) == 0:
        mp = ml = pessoas[1]
    else:
        if pessoas[1] > mp:
            mp = pessoas[1]
        if pessoas[1] < ml:
            ml = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()
    while True:
        u = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
        if u in 'SN':
            break
    if u == 'N':
        break
print('-='*40)
print(f'Ao todo você cadastrou {len(dados)}!')
print(f'O maior peso foi de {mp}. São:', end='')
for p in dados:
    if p[1] == mp:
        print(f' [{p[0]}] ', end='')
print()
print(f'O menor peso foi de {ml}. São: ', end='')
for p in dados:
    if p[1] == ml:
        print(f' [{p[0]}] ', end='')