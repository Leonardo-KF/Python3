t1 = int(input('Digite o primeiro termo de uma progressão aritmética: '))
r = int(input('Digite a RAZÃO da progressão: '))
termo = t1 + (10 - 1) * r
print('Os 10 primeiros termos dessa progressão são: ')
for p in range(t1, termo + r, r):
    print(f' {p}', end=' ->')
print(' Fim')
