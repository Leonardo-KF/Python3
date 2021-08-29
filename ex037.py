n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite qual a base de conversão desejada\n'
               '[1] Binário\n'
               '[2] Octal\n'
               '[3] Hexadecimal\n'
               'Digite a opção desejada: '))
if n2 == 1:
    print(f'{n1} Convertido para BINÁRIO é: {bin(n1)[2:]}')
elif n2 == 2:
    print(f'{n1} Convertido para OCTAL é: {oct(n1)[2:]}')
elif n2 == 3:
    print(f'{n1} Convertido para HEXADECIMAL é: {hex(n1)[2:]}')
else:
    print('Opção invalida, tente novamente!')