num = (int(input('Digite o primeiro numero: ')),
       int(input('Digite o segundo numero: ')),
       int(input('Digite o terceiro numero: ')),
       int(input('Digite o ultimo numero: ')))
print(f'Os numeros digitados foram {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 aparece na {num.index(3) + 1}ª posição')
else:
    print('O numero 3 não foi digitado!')
print('Os numeros pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')