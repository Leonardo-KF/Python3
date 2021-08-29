s = 0
c = 0
for l in range(1, 7):
    n1 = int(input(f'Digite o {l}° numero inteiro: '))
    if n1 % 2 == 0:
        c += 1
        s = s + n1
print(f'A soma dos {c} numeros pares é: {s}')
