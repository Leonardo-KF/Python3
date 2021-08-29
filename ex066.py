soma = cont = 0
while True:
    n1 = int(input('Digite um numero (999 para): '))
    if n1 == 999:
        break
    soma += n1
    cont += 1
print(f'Foram calculados {cont} numeros e a soma deles é: {soma}')
