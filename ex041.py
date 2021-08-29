from datetime import date
n1 = int(input('Digite o seu ano de nascimento: '))
anos = date.today().year - n1
if anos <= 9:
    categ = 'Mirim'
elif anos <= 14:
    categ = 'Infantil'
elif anos <= 19:
    categ = 'Junior'
elif anos <= 25:
    categ = 'Sênior'
elif anos > 25:
    categ = 'Master'
print(f'Sua categoria é: {categ}!')
