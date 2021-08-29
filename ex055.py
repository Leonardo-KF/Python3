map = 0
mep = 0
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}° pessoa: '))
    if p == 1:
        map = peso
        mep = peso
    else:
        if peso > map:
            map = peso
        if peso < mep:
            mep = peso
print(f'O maior peso lido foi de: {map}Kg\n'
      f'O menor peso lido foi de: {mep}Kg')

