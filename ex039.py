from datetime import date
i1 = int(input('Digite o ano do seu nascimento: '))
anos = date.today().year - i1
if anos < 17:
    print('Você ainda irá se alistar!')
    print(f'Faltam {18 - anos} anos para o seu alistamento!')
elif anos == 18:
    print('Você tem que se alistar nesse ano!')
else:
    print('Ja passou o tempo do seu alistamento!')
    print(f'Voce deveria ter se alistado ja fazem {anos - 18} anos!')
