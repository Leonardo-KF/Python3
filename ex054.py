from datetime import date
c1 = 0
c2 = 0
for p in range(1, 8):
    nasc = int(input(f'Em que ano a {p}° pessoa nasceu: '))
    id = date.today().year - nasc
    if id <= 21:
        c1 += 1
    else:
        c2 += 1
print(f'{c1} São menores e {c2} são maiores')