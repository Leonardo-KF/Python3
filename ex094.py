pes = {}
pessoas = []
idades = 0
while True:
    pes.clear()
    pes['nome'] = str(input('Nome: '))
    while True:
        pes['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pes['sexo'] in 'MF':
            break
        print('Escolha inválida! Por favor digite M ou F')
    pes['idade'] = int(input('Idade: '))
    idades += pes['idade']
    pessoas.append(pes.copy())
    while True:
        u = str(input('Quer continuar [S/N]: ')).strip().upper()
        if u in 'SN':
            break
        print('Escolha inválida! Por favor digite S ou N!')
    if u == 'N':
        break
print(f'Foram cadastradas no total {len(pessoas)} pessoas!')
mulheres = []
pam = []
for i, d in enumerate(pessoas):
    if pessoas[i]['sexo'] == 'F':
        mulheres.append(pessoas[i]['nome'][:])
    if pessoas[i]['idade'] > (idades / len(pessoas)):
        pam.append(pessoas[i].copy())
print('='*40)
print(f'A média de idade das pessoas cadastradas foi {idades / len(pessoas):.2f}')
print('As mulheres cadastradas foram: ', end='')
for c in mulheres:
    print(f'{c}', end=' ')
print()
print(f'As pessoas com idade acima da média são: ')
for i, v in enumerate(pam):
    print(f'=> Nome;{v["nome"]:^8} Sexo;{v["sexo"]:^8}  Idade:{v["idade"]:^8}')
