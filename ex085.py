valores = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}° numero: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
print('='*30)
print(f'Os valores pares são: {sorted(valores[0])}')
print(f'Os valores ímpares são: {sorted(valores[1])}')
