n1 = str(input('Digite seu nome completo: ')).strip()
print('Analisando...')
n2 = n1.split()
n3 = n1.upper()
n4 = n1.lower()
n5 = len(n1) - n1.count(' ')
n6 = len(n2[0])
print(f'Seu nome em maiusculas é: {n3}')
print(f'Seu nome em minusculas é: {n4}')
print(f'Seu nome tem ao todo {n5} letras')
print(f'O seu primeiro nome tem {n6} letras!')