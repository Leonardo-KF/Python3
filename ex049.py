n1 = int(input('Digite o numero que deseja a tabuada: '))
print(f'A tabuada de {n1} é:')
for c in range(1, 11):
    r = n1 * c
    print(f'{c} X {n1} = {r}')
