print('='*15)
print('BANCO DO PYTHON')
print('='*15)
v1 = int(input('Digite o valor que deseja sacar R$: '))
ced = 50
contced = 0
total = v1
while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        if contced > 0:
            print(f'Serão entregues {contced} notas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contced = 0
        if total == 0:
            break

