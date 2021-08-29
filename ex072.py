num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
n1 = int(input('Digite um numero de 0 a 10: '))
while n1 > 10 or n1 < 0:
    n1 = int(input('Digite novamente um numero de 0 a 10: '))
print(f'Você digitou o numero: {num[n1]}')