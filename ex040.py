n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m1 = (n1 + n2) / 2
if m1 < 5:
    print(f'Sua média foi {m1} e você foi reprovado!')
elif 5 < m1 < 7:
    print(f'Sua média foi {m1} e você terá que fazer a recuperação!')
else:
    print(f'Sua média foi de {m1} e você foi aprovado! Parabéns!')
