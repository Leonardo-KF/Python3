p1 = str(input('Digite a frase: ')).strip().upper()
pal1 = p1.split()
jun1 = ''.join(pal1)
inv = jun1[::-1]
'''inv = ''
for letra in range(len(jun1) - 1, -1, -1):
    inv += jun1[letra]'''
print(f'O inverso de {jun1} é {inv}!')
if inv == jun1:
    print('É um palindromo!')
else:
    print('Não é um palindromo!')