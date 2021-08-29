from  math import hypot
ca = float(input('Digite o valor do cateto adjascente: '))
co = float(input('Digite o valor do cateto oposto: '))
hi = hypot(ca, co)
print(f'O valor da hipotenusa é: {hi:.2f}')
