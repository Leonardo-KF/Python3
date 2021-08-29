cont = 0
n1 = int(input('Digite um numero: '))
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print(f'\33[33m {c}', end='')
        cont += 1
    else:
        print(f'\33[36m {c}', end='')
print(f'\n\033[mO {n1} Foi dividido {cont} vezes!')
if cont > 2:
    print(f'\nnumero {n1} não é primo!')
else:
    print(f'O numero {n1} é primo!')
