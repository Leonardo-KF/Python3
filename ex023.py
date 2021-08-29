num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O numero tem: \n')
print(f'{u} Unidades')
print(f'{d} Dezenas')
print(f'{c} Centenas')
print(f'{m} milhares')
