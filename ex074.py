from random import randint
a = randint(1, 10)
b = randint(1, 10)
c = randint(1, 10)
d = randint(1, 10)
e = randint(1, 10)
num = (a, b, c, d, e)
menor = a
maior = a
co = 0
while co != 4:
    co += 1
    if maior < num[co]:
        maior = num[co]
    if menor > num[co]:
        menor = num[co]
print(f'Os numeros escolhidos foram {num}')
print(f'O maior deles é {maior}\n'
      f'E o menor é {menor}')