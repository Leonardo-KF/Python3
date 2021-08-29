n1 = int(input('Quantos termos voce deseja da sequencia de fibonacci: '))
t1 = 0
t2 = 1
t3 = 0
cont = 2
print(f'{t1}->{t2}->', end='')
while cont < n1:
    t3 = t1 + t2
    cont += 1
    print(f'{t3}->', end='')
    t1 = t2
    t2 = t3
print('Fim!')
