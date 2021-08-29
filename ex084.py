dados = list()
pessoas = list()
mp = ml = 0
np = list()
nl = list()
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso em kg: ')))
    dados.append(pessoas[:])
    pessoas.clear()
    while True:
        u = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
        if u in 'SN':
            break
    if u == 'N':
        break
for p in dados:
    if p == dados[0]:
        ml = p[1]
        nl.append(p[0])
        mp = p[1]
        np.append(p[0])
    elif p[1] == mp:
        np.append(p[0])
    elif p[1] == ml:
        nl.append(p[0])
    else:
        if p[1] > mp:
            mp = p[1]
            np.clear()
            np.append(p[0])
        if p[1] < ml:
            ml = p[1]
            nl.clear()
            nl.append(p[0])
print('=' * 38)
print(f'O numero de pessoas cadastradas foi {len(dados)}!')
print('=' * 38)
print(f'As pessoas mais pesadas pesam {mp}kg e são: {np}')
print('=' * 38)
print(f'As mais leves pesam {ml}kg e são: {nl}')
