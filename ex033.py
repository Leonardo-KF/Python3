n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
# tentiva inicial

'''if n1 >= n2 and n1 >= n3:
    print(f'O maior numero é: {n1}')
if n2 >= n1 and n2 >= n3:
    print(f'O maior numero é: {n2}')
if n3 >= n1 and n3 >= n2:
    print(f'O maior numero é: {n3}')
if n1 <= n2 and n1 <= n3:
    print(f'E o menor numero é: {n1}')
if n2 <= n1 and n2 <= n3:
    print(f'E o menor numero é: {n2}')
if n3 <= n1 and n3 <= n2:
    print(f'E o menor numero é: {n3}')'''
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n3
if n1 > n3 and n1 > n2:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
print(f'O menor valor digitado foi {menor}\nE o maior digitado foi {maior}')
