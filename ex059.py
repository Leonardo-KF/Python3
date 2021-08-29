from time import sleep
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
op = 0
res = 0
while op != 5:
    op = int(input('Digite a opção desejada:\n'
                   '[ 1 ] SOMA\n'
                   '[ 2 ] MULTIPLICAÇÃO\n'
                   '[ 3 ] MAIOR\n'
                   '[ 4 ] NOVOS NUMEROS\n'
                   '[ 5 ] SAIR\n'
                   'Sua escolha: '))
    if op == 1:
        res = num1 + num2
        print(f'A soma de: {num1} + {num2} é {res}')
    elif op == 2:
        res = num1 * num2
        print(f'A multiplicação de: {num1} x {num2} é {res}')
    elif op == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'Entre {num1} e {num2} o maior é {maior}')
    elif op == 4:
        num1 = int(input('Digite o 1° novo numero: '))
        num2 = int(input('Digite o 2° novo numero: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção invalida! Tente novamente!')
    print('-=-' * 15)
    sleep(1)