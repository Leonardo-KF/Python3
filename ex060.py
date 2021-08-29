n1 = int(input('Digite o numero que você deseja calcular a fatorial: '))
res = n1
r1 = 1
while res > 0:
    print(f'{res}', end='')
    print('x' if res > 1 else '=', end='')
    r1 = r1 * res
    res -= 1
print(r1)