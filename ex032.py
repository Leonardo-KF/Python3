from datetime import date
a1 = int(input('Digite o ano de sua preferência, para o ano atual digite 0: '))
if a1 == 0:
    a1 = date.today().year
if a1 % 4 == 0 and a1 % 100 != 0 or a1 % 400 == 0:
    print(f'{a1} É um ano bissexto!!')
else:
    print(f'{a1} Não é um ano bissexto!!')
