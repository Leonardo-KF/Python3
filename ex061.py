print('        Gerador de PA\n', '-=-' * 10)
ini = int(input('Digite o numero inicial: '))
r = int(input('Digite a razão: '))
cont = 0
while cont != 10:
    print(f'{ini} -> ', end='')
    ini += r
    cont += 1
print('Fim')