n1 = int(input('Digite o primeiro numero inteiro: '))
n2 = int(input('Digite o segundo numero inteiro: '))
if n1 > n2:
    print(f'O maior valor é: {n1}')
elif n2 > n1:
    print(f'O maior valor é: {n2}')
else:
    print(f'Não exite valor maior, os dois valores são iguais!')
