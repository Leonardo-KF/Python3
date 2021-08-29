matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = s3 = m2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um numero para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            sp += matriz[l][c]
        if matriz[l][2]:
            s3 += matriz[l][2]
for c in matriz[1]:
    if c == matriz[1][0] or c > m2:
        m2 = c
print('='*40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('='*40)
print(f'A soma de todos os valores pares digitados é: {sp}')
print(f'A soma dos valores da terceira coluna é: {s3}')
print(f'O maior valor da segunda linha é: {m2}')