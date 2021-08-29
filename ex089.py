geral = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2)/2
    geral.append([nome, [n1, n2], m])
    u = str(input('Deseja continuar? ')).strip().upper()[0]
    if u == 'N':
        break
print('='*30)
print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for i, c in enumerate(geral):
    print(f'{i:<4}{c[0]:<10}{c[2]:>7.1f}')
while True:
    u = int(input('Digite o N° do aluno que deseja ver as notas (999 para encerrar): '))
    if u == 999:
        print('Finalizando o programa!')
        break
    if u <= len(geral) - 1:
        print(f'As notas de {geral[u][0]} são: {geral[u][1]}')
    else:
        print('Opção invalida! Digite novamente.')