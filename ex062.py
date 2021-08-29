print('Gerador de PA')
n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
ad = 10
tot = 0
while ad != 0:
    tot = tot + ad
    while cont <= tot:
        print(f'{n1}->', end='')
        n1 += r
        cont += 1
    print('Pausa!')
    ad = int(input('Você deseja mais quantos termos? '))
print(f'Operação finalizada mostrando {tot} termos!')