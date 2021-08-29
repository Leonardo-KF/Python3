cont = 0
n1 = 0
soma = 0
while n1 != 999:
    n1 = int(input('Digite um numero (999 para parar): '))
    if n1 != 999:
        soma += n1
        cont += 1
print(f'A soma dos {cont} numeros é: {soma}')